# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: worker/v1/step_executor.proto
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
    'worker/v1/step_executor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.transport.v1 import transport_pb2 as transport_dot_v1_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dworker/v1/step_executor.proto\x12\tworker.v1\x1a\x1ctransport/v1/transport.proto\"#\n\x0bStringValue\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value2\xd3\x02\n\x13StepExecutorService\x12;\n\x06Stream\x12\x15.transport.v1.Request\x1a\x16.worker.v1.StringValue\"\x00\x30\x01\x12:\n\x07\x45xecute\x12\x15.transport.v1.Request\x1a\x16.transport.v1.Response\"\x00\x12;\n\x08Metadata\x12\x15.transport.v1.Request\x1a\x16.transport.v1.Response\"\x00\x12\x41\n\x0eTestConnection\x12\x15.transport.v1.Request\x1a\x16.transport.v1.Response\"\x00\x12\x43\n\x10\x44\x65leteDatasource\x12\x15.transport.v1.Request\x1a\x16.transport.v1.Response\"\x00\x42\x39Z7github.com/superblocksteam/agent/types/gen/go/worker/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker.v1.step_executor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/superblocksteam/agent/types/gen/go/worker/v1'
  _globals['_STRINGVALUE']._serialized_start=74
  _globals['_STRINGVALUE']._serialized_end=109
  _globals['_STEPEXECUTORSERVICE']._serialized_start=112
  _globals['_STEPEXECUTORSERVICE']._serialized_end=451
# @@protoc_insertion_point(module_scope)
