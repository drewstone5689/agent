# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: event/v2/service.proto
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
    'event/v2/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from event.v2 import cloudevent_pb2 as event_dot_v2_dot_cloudevent__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x65vent/v2/service.proto\x12\x08\x65vent.v2\x1a\x19\x65vent/v2/cloudevent.proto\x1a\x1bgoogle/protobuf/empty.proto2\x84\x01\n\rEventsService\x12;\n\x07Receive\x12\x16.google.protobuf.Empty\x1a\x14.event.v2.CloudEvent\"\x00\x30\x01\x12\x36\n\x04Send\x12\x14.event.v2.CloudEvent\x1a\x16.google.protobuf.Empty\"\x00\x42\x38Z6github.com/superblocksteam/agent/types/gen/go/event/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'event.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/superblocksteam/agent/types/gen/go/event/v2'
  _globals['_EVENTSSERVICE']._serialized_start=93
  _globals['_EVENTSSERVICE']._serialized_end=225
# @@protoc_insertion_point(module_scope)
