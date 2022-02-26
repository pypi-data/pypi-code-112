# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: okapi/transport/v1/transport.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class SignRequest(betterproto.Message):
    payload: bytes = betterproto.bytes_field(1)
    key: "__keys_v1__.JsonWebKey" = betterproto.message_field(2)
    append_to: "___pbmse_v1__.SignedMessage" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class SignResponse(betterproto.Message):
    message: "___pbmse_v1__.SignedMessage" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class VerifyRequest(betterproto.Message):
    message: "___pbmse_v1__.SignedMessage" = betterproto.message_field(1)
    key: "__keys_v1__.JsonWebKey" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class VerifyResponse(betterproto.Message):
    is_valid: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class PackRequest(betterproto.Message):
    sender_key: "__keys_v1__.JsonWebKey" = betterproto.message_field(1)
    receiver_key: "__keys_v1__.JsonWebKey" = betterproto.message_field(2)
    associated_data: bytes = betterproto.bytes_field(3)
    plaintext: bytes = betterproto.bytes_field(4)
    mode: "___pbmse_v1__.EncryptionMode" = betterproto.enum_field(5)
    algorithm: "___pbmse_v1__.EncryptionAlgorithm" = betterproto.enum_field(6)


@dataclass(eq=False, repr=False)
class PackResponse(betterproto.Message):
    message: "___pbmse_v1__.EncryptedMessage" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class UnpackRequest(betterproto.Message):
    sender_key: "__keys_v1__.JsonWebKey" = betterproto.message_field(1)
    receiver_key: "__keys_v1__.JsonWebKey" = betterproto.message_field(2)
    message: "___pbmse_v1__.EncryptedMessage" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class UnpackResponse(betterproto.Message):
    plaintext: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class CoreMessage(betterproto.Message):
    id: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    body: bytes = betterproto.bytes_field(3)
    to: List[str] = betterproto.string_field(4)
    from_: str = betterproto.string_field(5)
    created: int = betterproto.int64_field(6)
    expires: int = betterproto.int64_field(7)


from ....pbmse import v1 as ___pbmse_v1__
from ...keys import v1 as __keys_v1__
