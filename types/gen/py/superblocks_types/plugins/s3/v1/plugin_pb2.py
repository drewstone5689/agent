# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plugins/s3/v1/plugin.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'plugins/s3/v1/plugin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aplugins/s3/v1/plugin.proto\x12\rplugins.s3.v1\";\n\x13SuperblocksMetadata\x12$\n\rpluginVersion\x18\x01 \x01(\tR\rpluginVersion\"\xbe\x02\n\x08Property\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value\x12\x1a\n\x08\x65\x64itable\x18\x03 \x01(\x08R\x08\x65\x64itable\x12\x1a\n\x08internal\x18\x04 \x01(\x08R\x08internal\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x1c\n\tmandatory\x18\x06 \x01(\x08R\tmandatory\x12\x12\n\x04type\x18\x07 \x01(\tR\x04type\x12\"\n\x0c\x64\x65\x66\x61ultValue\x18\x08 \x01(\tR\x0c\x64\x65\x66\x61ultValue\x12\x1a\n\x08minRange\x18\t \x01(\tR\x08minRange\x12\x1a\n\x08maxRange\x18\n \x01(\tR\x08maxRange\x12\"\n\x0cvalueOptions\x18\x0b \x03(\tR\x0cvalueOptions\"S\n\x06\x43ustom\x12I\n\x13presignedExpiration\x18\x01 \x01(\x0b\x32\x17.plugins.s3.v1.PropertyR\x13presignedExpiration\"\xaf\x02\n\x06Plugin\x12\x1a\n\x08resource\x18\x01 \x01(\tR\x08resource\x12\x16\n\x06\x61\x63tion\x18\x02 \x01(\tR\x06\x61\x63tion\x12\x12\n\x04path\x18\x03 \x01(\tR\x04path\x12\x12\n\x04\x62ody\x18\x04 \x01(\tR\x04\x62ody\x12 \n\x0b\x66ileObjects\x18\x05 \x01(\tR\x0b\x66ileObjects\x12\"\n\x0cresponseType\x18\x06 \x01(\tR\x0cresponseType\x12-\n\x06\x63ustom\x18\x07 \x01(\x0b\x32\x15.plugins.s3.v1.CustomR\x06\x63ustom\x12T\n\x13superblocksMetadata\x18\x08 \x01(\x0b\x32\".plugins.s3.v1.SuperblocksMetadataR\x13superblocksMetadataB=Z;github.com/superblocksteam/agent/types/gen/go/plugins/s3/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.s3.v1.plugin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/superblocksteam/agent/types/gen/go/plugins/s3/v1'
  _globals['_SUPERBLOCKSMETADATA']._serialized_start=45
  _globals['_SUPERBLOCKSMETADATA']._serialized_end=104
  _globals['_PROPERTY']._serialized_start=107
  _globals['_PROPERTY']._serialized_end=425
  _globals['_CUSTOM']._serialized_start=427
  _globals['_CUSTOM']._serialized_end=510
  _globals['_PLUGIN']._serialized_start=513
  _globals['_PLUGIN']._serialized_end=816
# @@protoc_insertion_point(module_scope)
