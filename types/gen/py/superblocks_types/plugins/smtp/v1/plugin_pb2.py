# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plugins/smtp/v1/plugin.proto
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
    'plugins/smtp/v1/plugin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.plugins.common.v1 import plugin_pb2 as plugins_dot_common_dot_v1_dot_plugin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cplugins/smtp/v1/plugin.proto\x12\x0fplugins.smtp.v1\x1a\x1eplugins/common/v1/plugin.proto\"\xdd\x04\n\x06Plugin\x12\x17\n\x04name\x18\x01 \x01(\tH\x00R\x04name\x88\x01\x01\x12\x46\n\nconnection\x18\x02 \x01(\x0b\x32&.plugins.smtp.v1.Plugin.SmtpConnectionR\nconnection\x12\x12\n\x04\x66rom\x18\x03 \x01(\tR\x04\x66rom\x12\x19\n\x08reply_to\x18\x04 \x01(\tR\x07replyTo\x12\x0e\n\x02to\x18\x05 \x01(\tR\x02to\x12\x0e\n\x02\x63\x63\x18\x06 \x01(\tR\x02\x63\x63\x12\x10\n\x03\x62\x63\x63\x18\x07 \x01(\tR\x03\x62\x63\x63\x12\x18\n\x07subject\x18\x08 \x01(\tR\x07subject\x12\x12\n\x04\x62ody\x18\t \x01(\tR\x04\x62ody\x12 \n\x0b\x61ttachments\x18\n \x01(\tR\x0b\x61ttachments\x12z\n\x1e\x64ynamic_workflow_configuration\x18\x0b \x01(\x0b\x32/.plugins.common.v1.DynamicWorkflowConfigurationH\x01R\x1c\x64ynamicWorkflowConfiguration\x88\x01\x01\x1a\x98\x01\n\x0eSmtpConnection\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\x05R\x04port\x12\x1a\n\x08username\x18\x03 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x04 \x01(\tR\x08password\x12\x1b\n\x06secure\x18\x05 \x01(\x08H\x00R\x06secure\x88\x01\x01\x42\t\n\x07_secureB\x07\n\x05_nameB!\n\x1f_dynamic_workflow_configurationB?Z=github.com/superblocksteam/agent/types/gen/go/plugins/smtp/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.smtp.v1.plugin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/superblocksteam/agent/types/gen/go/plugins/smtp/v1'
  _globals['_PLUGIN']._serialized_start=82
  _globals['_PLUGIN']._serialized_end=687
  _globals['_PLUGIN_SMTPCONNECTION']._serialized_start=491
  _globals['_PLUGIN_SMTPCONNECTION']._serialized_end=643
# @@protoc_insertion_point(module_scope)
