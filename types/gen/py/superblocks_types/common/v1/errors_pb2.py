# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/v1/errors.proto
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
    'common/v1/errors.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63ommon/v1/errors.proto\x12\tcommon.v1\"\xb0\x01\n\x05\x45rror\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07handled\x18\x03 \x01(\x08R\x07handled\x12\x1d\n\nblock_path\x18\x04 \x01(\tR\tblockPath\x12\x1b\n\tform_path\x18\x05 \x01(\tR\x08\x66ormPath\x12#\n\x04\x63ode\x18\x06 \x01(\x0e\x32\x0f.common.v1.CodeR\x04\x63ode*\xcd\x02\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\"\n\x1e\x43ODE_INTEGRATION_AUTHORIZATION\x10\x01\x12\x1c\n\x18\x43ODE_INTEGRATION_NETWORK\x10\x02\x12\"\n\x1e\x43ODE_INTEGRATION_QUERY_TIMEOUT\x10\x03\x12\x1b\n\x17\x43ODE_INTEGRATION_SYNTAX\x10\x04\x12\x1a\n\x16\x43ODE_INTEGRATION_LOGIC\x10\x05\x12+\n\'CODE_INTEGRATION_MISSING_REQUIRED_FIELD\x10\x06\x12\x1f\n\x1b\x43ODE_INTEGRATION_RATE_LIMIT\x10\x07\x12#\n\x1f\x43ODE_INTEGRATION_USER_CANCELLED\x10\x08\x12\x1d\n\x19\x43ODE_INTEGRATION_INTERNAL\x10\tB9Z7github.com/superblocksteam/agent/types/gen/go/common/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/superblocksteam/agent/types/gen/go/common/v1'
  _globals['_CODE']._serialized_start=217
  _globals['_CODE']._serialized_end=550
  _globals['_ERROR']._serialized_start=38
  _globals['_ERROR']._serialized_end=214
# @@protoc_insertion_point(module_scope)
