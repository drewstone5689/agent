# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event/v1/service.proto
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
    'event/v1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x65vent/v1/service.proto\x12\x08\x65vent.v1\",\n\x12IngestEventRequest\x12\x16\n\x06\x65vents\x18\x01 \x03(\x0cR\x06\x65vents\"\xa9\x01\n\x13IngestEventResponse\x12\x18\n\x07success\x18\x01 \x01(\x05R\x07success\x12\x42\n\x06\x65rrors\x18\x02 \x03(\x0b\x32*.event.v1.IngestEventResponse.ErrorWrapperR\x06\x65rrors\x1a\x34\n\x0c\x45rrorWrapper\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05\x65rror\x18\x02 \x01(\tR\x05\x65rrorB8Z6github.com/superblocksteam/agent/types/gen/go/event/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/superblocksteam/agent/types/gen/go/event/v1'
  _globals['_INGESTEVENTREQUEST']._serialized_start=36
  _globals['_INGESTEVENTREQUEST']._serialized_end=80
  _globals['_INGESTEVENTRESPONSE']._serialized_start=83
  _globals['_INGESTEVENTRESPONSE']._serialized_end=252
  _globals['_INGESTEVENTRESPONSE_ERRORWRAPPER']._serialized_start=200
  _globals['_INGESTEVENTRESPONSE_ERRORWRAPPER']._serialized_end=252
# @@protoc_insertion_point(module_scope)
