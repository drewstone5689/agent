# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: syncer/v1/syncer.proto
# Protobuf Python Version: 5.27.4
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    4,
    '',
    'syncer/v1/syncer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.ai.v1 import metadata_pb2 as ai_dot_v1_dot_metadata__pb2
from superblocks_types.buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from superblocks_types.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16syncer/v1/syncer.proto\x12\tsyncer.v1\x1a\x14\x61i/v1/metadata.proto\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\x82\x03\n\x08Metadata\x12\x39\n\x10\x63onfiguration_id\x18\x01 \x01(\tB\x0e\xfa\x42\x04r\x02\x10\x01\xbaH\x04r\x02\x10\x01R\x0f\x63onfigurationId\x12\x35\n\x0eintegration_id\x18\x02 \x01(\tB\x0e\xfa\x42\x04r\x02\x10\x01\xbaH\x04r\x02\x10\x01R\rintegrationId\x12\x42\n\x0craw_metadata\x18\x03 \x01(\x0b\x32\x0f.ai.v1.MetadataB\x0e\xfa\x42\x05\x8a\x01\x02\x10\x01\xbaH\x03\xc8\x01\x01R\x0brawMetadata\x12L\n\x14updated_datetime_utc\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x12updatedDatetimeUtc\x12\x39\n\x10integration_type\x18\x05 \x01(\tB\x0e\xfa\x42\x04r\x02\x10\x01\xbaH\x04r\x02\x10\x01R\x0fintegrationType\x12\x37\n\x0forganization_id\x18\x06 \x01(\tB\x0e\xfa\x42\x04r\x02\x10\x01\xbaH\x04r\x02\x10\x01R\x0eorganizationIdB9Z7github.com/superblocksteam/agent/types/gen/go/syncer/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'syncer.v1.syncer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/superblocksteam/agent/types/gen/go/syncer/v1'
  _globals['_METADATA'].fields_by_name['configuration_id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['configuration_id']._serialized_options = b'\372B\004r\002\020\001\272H\004r\002\020\001'
  _globals['_METADATA'].fields_by_name['integration_id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['integration_id']._serialized_options = b'\372B\004r\002\020\001\272H\004r\002\020\001'
  _globals['_METADATA'].fields_by_name['raw_metadata']._loaded_options = None
  _globals['_METADATA'].fields_by_name['raw_metadata']._serialized_options = b'\372B\005\212\001\002\020\001\272H\003\310\001\001'
  _globals['_METADATA'].fields_by_name['integration_type']._loaded_options = None
  _globals['_METADATA'].fields_by_name['integration_type']._serialized_options = b'\372B\004r\002\020\001\272H\004r\002\020\001'
  _globals['_METADATA'].fields_by_name['organization_id']._loaded_options = None
  _globals['_METADATA'].fields_by_name['organization_id']._serialized_options = b'\372B\004r\002\020\001\272H\004r\002\020\001'
  _globals['_METADATA']._serialized_start=147
  _globals['_METADATA']._serialized_end=533
# @@protoc_insertion_point(module_scope)
