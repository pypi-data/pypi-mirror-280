import base64
import copy
import logging
import time
import typing

import kubernetes.client
import kubernetes.config

import cfg_mgmt
import cfg_mgmt.util
import ci.util
import model
import model.kubernetes

from cfg_mgmt.model import (
    CfgQueueEntry,
    ValidationError,
)
from kubernetes.client import (
    CoreV1Api,
    V1ObjectMeta,
    V1Secret,
    V1ServiceAccount,
)


ci.log.configure_default_logging()
logger = logging.getLogger(__name__)


def rotate_cfg_element(
    cfg_element: model.kubernetes.KubernetesConfig,
    cfg_factory: model.ConfigFactory,
) ->  typing.Tuple[cfg_mgmt.revert_function, dict, model.NamedModelElement]:

    # TODO: Cannot rotate kubeconfig without SA

    # copy passed cfg_element, since we update in-place.
    raw_cfg = copy.deepcopy(cfg_element.raw)
    cfg_to_rotate = model.kubernetes.KubernetesConfig(
        name=cfg_element.name(), raw_dict=raw_cfg, type_name=cfg_element._type_name
    )

    api_client = kubernetes.config.new_client_from_config_dict(cfg_element.kubeconfig())
    core_api = CoreV1Api(api_client)

    # find service-account
    service_account_config = cfg_to_rotate.service_account()

    sa: V1ServiceAccount = core_api.read_namespaced_service_account(
        name=service_account_config.name(),
        namespace=service_account_config.namespace(),
    )

    if cfg_element.rotation_strategy() == model.kubernetes.RotationStrategy.TOKEN_REQUEST:
        if not (bound_secret_name := cfg_to_rotate.raw.get('bound_secret_name')):
            raise ValueError(
                'Token request rotation requires attribute "bound_secret_name" in kubernetes-cfg.'
            )

        secret_id = {
            'old_tokens': [{"name": bound_secret_name}],
        }

        binding_secret_name = _create_secret_for_token_bind(
            core_api=core_api,
            service_account=sa,
        )

        expiration_seconds = 60 * 60 * 24 * 90 # 7776000s = 90d is max
        new_sa_access_token = core_api.create_namespaced_service_account_token(
            name=service_account_config.name(),
            namespace=service_account_config.namespace(),
            body={
                "spec": {"expirationSeconds": expiration_seconds},
                "bound_object_ref": {"name": binding_secret_name, "kind": "Secret"},
            },
        )

        if not new_sa_access_token:
            # the token was not created for service account. Clean up
            # and raise
            core_api.delete_namespaced_secret(
                name=binding_secret_name,
                namespace=service_account_config.namespace(),
            )
            raise RuntimeError('Error creating new service account token.')

        # update kubeconfig with new token
        cfg_to_rotate.kubeconfig()["users"][0]["user"]["token"] = new_sa_access_token.status.token

        cfg_to_rotate.raw["bound_secret_name"] = binding_secret_name

        def revert():
            logger.warning(
                f"An error occurred during update of kubernetes config '{cfg_to_rotate.name()}', "
                'rolling back'
            )

            # delete newly created service-account token
            core_api.delete_namespaced_secret(
                name=binding_secret_name,
                namespace=service_account_config.namespace(),
            )

    elif cfg_element.rotation_strategy() == model.kubernetes.RotationStrategy.SECRET:
        old_tokens = [{"name": token.name} for token in sa.secrets] if sa.secrets else []
        secret_id = {
            'old_tokens': old_tokens,
        }

        # create new token
        new_access_token_name = _create_token_for_sa(
            core_api=core_api,
            service_account=sa,
        )

        new_access_token = _wait_for_token_secret(
            core_api=core_api,
            token_name=new_access_token_name,
            token_namespace=service_account_config.namespace(),
        )

        if not new_access_token:
            # the cluster controller did not update the secret in the given time. Clean up
            # and raise
            core_api.delete_namespaced_secret(
                new_access_token_name,
                service_account_config.namespace(),
            )
            raise RuntimeError(
                'Service account token-secret was not populated with the required data in time.'
            )

        # patch service-account with new secret (this updates the secret that will be mounted to
        # k8s-pods)
        patched_sa = _update_sa(
            core_api=core_api,
            service_account=sa,
            token_list=[{'name': new_access_token_name}]
        )

        # create new kubeconfig from new access token
        updated_kubeconfig = _update_kubeconfig(
            kubeconfig=cfg_element.kubeconfig(),
            patched_service_account=patched_sa,
            new_access_token=new_access_token,
        )
        cfg_to_rotate.raw['kubeconfig'] = updated_kubeconfig

        def revert():
            logger.warning(
                f"An error occurred during update of kubernetes config '{cfg_to_rotate.name()}', "
                'rolling back'
            )
            # revert changes to service-account
            _update_sa(
                core_api=core_api,
                service_account=patched_sa,
                token_list=old_tokens,
            )

            # delete newly created service-account token
            _delete_sa_token(
                core_api=core_api,
                namespace=service_account_config.namespace(),
                token_name=new_access_token_name,
            )

    else:
        raise NotImplementedError(f'{cfg_element.rotation_strategy()=}')

    return revert, secret_id, cfg_to_rotate


def _update_sa(
    core_api: CoreV1Api,
    service_account: V1ServiceAccount,
    token_list: typing.List[dict],
) -> V1ServiceAccount:
    service_account_name = service_account.metadata.name
    service_account_namespace = service_account.metadata.namespace
    body = [{
        "op": "replace",
        "path": "/secrets",
        "value": token_list,
    }]
    return core_api.patch_namespaced_service_account(
        name=service_account_name,
        namespace=service_account_namespace,
        body=body,
    )


def _create_token_for_sa(
    core_api: CoreV1Api,
    service_account: V1ServiceAccount,
) -> str:
    service_account_name = service_account.metadata.name
    service_account_namespace = service_account.metadata.namespace
    token = core_api.create_namespaced_secret(
        namespace=service_account_namespace,
        body=V1Secret(
            api_version='v1',
            kind='Secret',
            metadata=V1ObjectMeta(
                generate_name=f'{service_account_name}-token-',
                annotations={'kubernetes.io/service-account.name': service_account_name},
            ),
            type='kubernetes.io/service-account-token',
        ),
    )
    # not all required values are set on the returned object yet. Return only name so that we can
    # fetch it later (name will be generated by the kube-apiserver)
    return token.metadata.name


def _create_secret_for_token_bind(
    core_api: CoreV1Api,
    service_account: V1ServiceAccount,
) -> str:
    service_account_name = service_account.metadata.name
    service_account_namespace = service_account.metadata.namespace
    token = core_api.create_namespaced_secret(
        namespace=service_account_namespace,
        body=V1Secret(
            api_version='v1',
            kind='Secret',
            metadata=V1ObjectMeta(
                generate_name=f'{service_account_name}-token-bind-',
            ),
            type='Opaque',
        ),
    )
    # not all required values are set on the returned object yet. Return only name so that we can
    # store it for deleting on next rotation
    return token.metadata.name


def _delete_sa_token(
    core_api: CoreV1Api,
    token_name: str,
    namespace: str,
):
    core_api.delete_namespaced_secret(
        name=token_name,
        namespace=namespace,
    )


def _update_kubeconfig(
    kubeconfig: dict,
    patched_service_account: V1ServiceAccount,
    new_access_token: V1Secret,
) -> dict:
    kubeconfig = copy.deepcopy(kubeconfig)

    sa_name = patched_service_account.metadata.name
    namespace = patched_service_account.metadata.namespace

    crt = new_access_token.data.get('ca.crt')
    token = new_access_token.data.get('token')
    kubeconfig['clusters'][0]['cluster']['certificate-authority-data'] = crt
    kubeconfig['users'] = [{
        'user': {'token': base64.b64decode(token).decode("utf-8")},
        'name': kubeconfig['contexts'][0]['context']['user']
    }]
    # Note: This is only our convention. We are free to choose whatever we want as far
    # as k8s is concerned (context-name is referred to as "nickname") as long as we use
    # it consistently.
    kubeconfig['contexts'][0]['name'] = f'system:serviceaccount:{namespace}:{sa_name}'
    kubeconfig['contexts'][0]['context']['namespace'] = namespace
    kubeconfig['current-context'] = f'system:serviceaccount:{namespace}:{sa_name}'

    return kubeconfig


def _wait_for_token_secret(
    core_api: CoreV1Api,
    token_name: str,
    token_namespace: str,
    retries: int = 3,
    interval: int = 5,
) -> typing.Union[V1Secret, None]:
    new_access_token = core_api.read_namespaced_secret(
        name=token_name,
        namespace=token_namespace,
    )
    if not new_access_token.data:
        logger.info('Access token was not yet populated with required information.')
        if retries > 0:
            logger.info(f'Will sleep for {interval} seconds and try again {retries} more times.')
            time.sleep(interval)
            return _wait_for_token_secret(
                core_api=core_api,
                token_name=token_name,
                token_namespace=token_namespace,
                retries=retries-1,
                interval=interval,
            )
        else:
            return None
    return new_access_token


def delete_config_secret(
    cfg_element: model.kubernetes.KubernetesConfig,
    cfg_factory: model.ConfigFactory,
    cfg_queue_entry: CfgQueueEntry,
) -> model.kubernetes.KubernetesConfig | None:
    api_client = kubernetes.config.new_client_from_config_dict(cfg_element.kubeconfig())
    core_api = CoreV1Api(api_client)

    for token in cfg_queue_entry.secretId['old_tokens']:
        _delete_sa_token(
            core_api=core_api,
            token_name=token['name'],
            namespace=cfg_element.service_account().namespace(),
        )

    return None


def validate_for_rotation(
    cfg_element: model.kubernetes.KubernetesConfig,
):
    if not cfg_element.service_account():
        raise ValidationError("Cannot rotate kubeconfigs without service account configs.")
    if len(cfg_element.kubeconfig()['contexts']) != 1:
        raise ValidationError("Rotation of kubeconfigs with multiple contexts is not implemented.")
