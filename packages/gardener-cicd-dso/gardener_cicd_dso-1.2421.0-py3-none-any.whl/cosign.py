# SPDX-FileCopyrightText: 2024 SAP SE or an SAP affiliate company and Gardener contributors
#
# SPDX-License-Identifier: Apache-2.0

import enum
import hashlib
import json
import logging

import ci.log
import ci.util
import oci.model as om
import oci.client as oc

ci.log.configure_default_logging()
logger = logging.getLogger(__name__)


class OnExist(enum.StrEnum):
    SKIP = 'skip'
    OVERWRITE = 'overwrite'


def payload_bytes(
    image_reference: om.OciImageReference | str,
    annotations: dict | None=None,
) -> bytes:
    '''
    returns payload for given OCI Image Reference + optional annotations as output by
    `cosign generate`

    Passed image-reference must have digest-tag.
    '''
    image_reference = om.OciImageReference.to_image_ref(image_reference)
    if not image_reference.has_digest_tag:
        raise ValueError('image-reference must have digest tag', image_reference)

    payload = {
        'critical': {
            'identity': {
                'docker-reference': image_reference.ref_without_tag,
            },
            'image': {
                'docker-manifest-digest': image_reference.tag,
            },
            'type': 'gardener.vnd/oci/cosign-signature',
        },
        'optional': annotations,
    }

    return json.dumps(
        obj=payload,
        separators=(',', ':'),
        sort_keys=True,
    ).encode('utf-8')


def default_signature_image_reference(
    image_ref: str,
) -> om.OciImageReference:
    '''
    calculate the (default) image reference of the cosign signature for a specific image.

    This image-reference is by default used/expected by cosign if no alternative signature
    repository is specified.
    '''
    parsed_image_ref = om.OciImageReference.to_image_ref(image_ref)
    if not parsed_image_ref.has_digest_tag:
        ValueError('only images that are referenced via digest are allowed')

    parsed_digest = parsed_image_ref.parsed_digest_tag
    alg, val = parsed_digest
    cosign_sig_ref = f'{parsed_image_ref.ref_without_tag}:{alg}-{val}.sig'

    return om.OciImageReference(cosign_sig_ref)


def sign_image(
    image_reference: om.OciImageReference | str,
    signature: str,
    on_exist: OnExist|str=OnExist.SKIP,
    signature_image_reference: str=None,
    oci_client: oc.Client=None,
):
    '''
    creates an OCI Image signature as understood by cosign
    '''
    on_exist = OnExist(on_exist)
    if not signature_image_reference:
        signature_image_reference = default_signature_image_reference(image_reference)

    if not oci_client:
        import ccc.oci
        oci_client = ccc.oci.oci_client()

    image_reference = om.OciImageReference.to_image_ref(image_reference)
    if not image_reference.has_tag:
        raise ValueError(image_reference, 'tag is required')
    if not image_reference.has_digest_tag:
        digest = hashlib.sha256(
            oci_client.manifest_raw(image_reference).content,
        ).hexdigest()
        image_reference = f'{image_reference.ref_without_tag}@sha256{digest}'

    if on_exist is OnExist.SKIP:
        if oci_client.head_manifest(
            image_reference=signature_image_reference,
            absent_ok=True,
        ):
            logger.info(f'signature exists: {signature_image_reference} - skipping')
            return

    # payload is normalised JSON w/ reference to signed image. It is expected as (only)
    # layer-blob for signature artefact
    payload = payload_bytes(
        image_reference=image_reference,
    )
    payload_size = len(payload)
    payload_digest = f'sha256:{hashlib.sha256(payload).hexdigest()}'

    oci_client.put_blob(
        image_reference=signature_image_reference,
        digest=payload_digest,
        octets_count=payload_size,
        data=payload,
    )

    # dummy cfg-blob as generated by cosign
    cfg_blob = json.dumps({
        'architecture': '',
        'config': {},
        'created': '0001-01-01T00:00:00Z',
        'history': [{'created': '0001-01-01T00:00:00Z'}],
        'os': '',
        'rootfs': {
            'diff_ids': [payload_digest],
            'type': 'layers',
        },
    },
        separators=(',', ':'),
        sort_keys=True,
    ).encode('utf-8')
    cfg_blob_size = len(cfg_blob)
    cfg_blob_digest = f'sha256:{hashlib.sha256(cfg_blob).hexdigest()}'

    oci_client.put_blob(
        image_reference=image_reference,
        digest=cfg_blob_digest,
        octets_count=cfg_blob_size,
        data=cfg_blob,
    )

    manifest = om.OciImageManifest(
        config=om.OciBlobRef(
            digest=cfg_blob_digest,
            mediaType='application/vnd.oci.image.config.v1+json',
            size=cfg_blob_size,
        ),
        mediaType='application/vnd.oci.image.manifest.v1+json',
        layers=[
            om.OciBlobRef(
                digest=payload_digest,
                size=payload_size,
                mediaType='application/vnd.dev.cosign.simplesigning.v1+json',
                annotations={
                    'dev.cosignproject.cosign/signature': signature,
                },
            ),
        ],
        annotations={},
    )

    manifest_bytes = json.dumps(manifest.as_dict()).encode('utf-8')

    oci_client.put_manifest(
        image_reference=signature_image_reference,
        manifest=manifest_bytes,
    )
