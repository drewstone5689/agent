# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plugins/cosmosdb/v1/plugin.proto
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
    'plugins/cosmosdb/v1/plugin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.plugins.common.v1 import auth_pb2 as plugins_dot_common_dot_v1_dot_auth__pb2
from superblocks_types.plugins.common.v1 import plugin_pb2 as plugins_dot_common_dot_v1_dot_plugin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n plugins/cosmosdb/v1/plugin.proto\x12\x13plugins.cosmosdb.v1\x1a\x1cplugins/common/v1/auth.proto\x1a\x1eplugins/common/v1/plugin.proto\"\x88\x10\n\x06Plugin\x12\x17\n\x04name\x18\x01 \x01(\tH\x01R\x04name\x88\x01\x01\x12z\n\x1e\x64ynamic_workflow_configuration\x18\x02 \x01(\x0b\x32/.plugins.common.v1.DynamicWorkflowConfigurationH\x02R\x1c\x64ynamicWorkflowConfiguration\x88\x01\x01\x12N\n\nconnection\x18\x03 \x01(\x0b\x32..plugins.cosmosdb.v1.Plugin.CosmosDbConnectionR\nconnection\x12\x33\n\x03sql\x18\x05 \x01(\x0b\x32\x1f.plugins.cosmosdb.v1.Plugin.SqlH\x00R\x03sql\x12U\n\x0fpoint_operation\x18\x06 \x01(\x0b\x32*.plugins.cosmosdb.v1.Plugin.PointOperationH\x00R\x0epointOperation\x1a\x8b\x01\n\x12\x43osmosDbConnection\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\x05R\x04port\x12\x1f\n\x0b\x64\x61tabase_id\x18\x03 \x01(\tR\ndatabaseId\x12,\n\x04\x61uth\x18\x04 \x01(\x0b\x32\x18.plugins.common.v1.AzureR\x04\x61uth\x1a\xbf\x02\n\x08Metadata\x12N\n\ncontainers\x18\x01 \x03(\x0b\x32..plugins.cosmosdb.v1.Plugin.Metadata.ContainerR\ncontainers\x1a\xe2\x01\n\tContainer\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12`\n\rpartition_key\x18\x02 \x01(\x0b\x32;.plugins.cosmosdb.v1.Plugin.Metadata.Container.PartitionKeyR\x0cpartitionKey\x1a\x63\n\x0cPartitionKey\x12\x14\n\x05paths\x18\x01 \x03(\tR\x05paths\x12\x12\n\x04kind\x18\x02 \x01(\tR\x04kind\x12\x1d\n\x07version\x18\x03 \x01(\x05H\x00R\x07version\x88\x01\x01\x42\n\n\x08_version\x1a\x86\x02\n\x03Sql\x12I\n\tsingleton\x18\x01 \x01(\x0b\x32).plugins.cosmosdb.v1.Plugin.Sql.SingletonH\x00R\tsingleton\x1a\xa9\x01\n\tSingleton\x12!\n\x0c\x63ontainer_id\x18\x01 \x01(\tR\x0b\x63ontainerId\x12\x14\n\x05query\x18\x02 \x01(\tR\x05query\x12\'\n\x0f\x63ross_partition\x18\x03 \x01(\x08R\x0e\x63rossPartition\x12(\n\rpartition_key\x18\x04 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_keyB\x08\n\x06\x61\x63tion\x1a\xf4\x06\n\x0ePointOperation\x12!\n\x0c\x63ontainer_id\x18\x01 \x01(\tR\x0b\x63ontainerId\x12\x45\n\x04read\x18\x02 \x01(\x0b\x32/.plugins.cosmosdb.v1.Plugin.PointOperation.ReadH\x00R\x04read\x12N\n\x07replace\x18\x03 \x01(\x0b\x32\x32.plugins.cosmosdb.v1.Plugin.PointOperation.ReplaceH\x00R\x07replace\x12K\n\x06upsert\x18\x04 \x01(\x0b\x32\x31.plugins.cosmosdb.v1.Plugin.PointOperation.UpsertH\x00R\x06upsert\x12K\n\x06\x64\x65lete\x18\x05 \x01(\x0b\x32\x31.plugins.cosmosdb.v1.Plugin.PointOperation.DeleteH\x00R\x06\x64\x65lete\x12K\n\x06\x63reate\x18\x06 \x01(\x0b\x32\x31.plugins.cosmosdb.v1.Plugin.PointOperation.CreateH\x00R\x06\x63reate\x1aR\n\x04Read\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12(\n\rpartition_key\x18\x03 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_key\x1aT\n\x06\x44\x65lete\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12(\n\rpartition_key\x18\x03 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_key\x1aY\n\x07Replace\x12\x12\n\x04\x62ody\x18\x01 \x01(\tR\x04\x62ody\x12(\n\rpartition_key\x18\x03 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_key\x1aX\n\x06Upsert\x12\x12\n\x04\x62ody\x18\x01 \x01(\tR\x04\x62ody\x12(\n\rpartition_key\x18\x03 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_key\x1aX\n\x06\x43reate\x12\x12\n\x04\x62ody\x18\x01 \x01(\tR\x04\x62ody\x12(\n\rpartition_key\x18\x03 \x01(\tH\x00R\x0cpartitionKey\x88\x01\x01\x42\x10\n\x0e_partition_keyB\x08\n\x06\x61\x63tionB\x11\n\x0f\x63osmosdb_actionB\x07\n\x05_nameB!\n\x1f_dynamic_workflow_configurationBCZAgithub.com/superblocksteam/agent/types/gen/go/plugins/cosmosdb/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.cosmosdb.v1.plugin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/superblocksteam/agent/types/gen/go/plugins/cosmosdb/v1'
  _globals['_PLUGIN']._serialized_start=120
  _globals['_PLUGIN']._serialized_end=2176
  _globals['_PLUGIN_COSMOSDBCONNECTION']._serialized_start=500
  _globals['_PLUGIN_COSMOSDBCONNECTION']._serialized_end=639
  _globals['_PLUGIN_METADATA']._serialized_start=642
  _globals['_PLUGIN_METADATA']._serialized_end=961
  _globals['_PLUGIN_METADATA_CONTAINER']._serialized_start=735
  _globals['_PLUGIN_METADATA_CONTAINER']._serialized_end=961
  _globals['_PLUGIN_METADATA_CONTAINER_PARTITIONKEY']._serialized_start=862
  _globals['_PLUGIN_METADATA_CONTAINER_PARTITIONKEY']._serialized_end=961
  _globals['_PLUGIN_SQL']._serialized_start=964
  _globals['_PLUGIN_SQL']._serialized_end=1226
  _globals['_PLUGIN_SQL_SINGLETON']._serialized_start=1047
  _globals['_PLUGIN_SQL_SINGLETON']._serialized_end=1216
  _globals['_PLUGIN_POINTOPERATION']._serialized_start=1229
  _globals['_PLUGIN_POINTOPERATION']._serialized_end=2113
  _globals['_PLUGIN_POINTOPERATION_READ']._serialized_start=1664
  _globals['_PLUGIN_POINTOPERATION_READ']._serialized_end=1746
  _globals['_PLUGIN_POINTOPERATION_DELETE']._serialized_start=1748
  _globals['_PLUGIN_POINTOPERATION_DELETE']._serialized_end=1832
  _globals['_PLUGIN_POINTOPERATION_REPLACE']._serialized_start=1834
  _globals['_PLUGIN_POINTOPERATION_REPLACE']._serialized_end=1923
  _globals['_PLUGIN_POINTOPERATION_UPSERT']._serialized_start=1925
  _globals['_PLUGIN_POINTOPERATION_UPSERT']._serialized_end=2013
  _globals['_PLUGIN_POINTOPERATION_CREATE']._serialized_start=2015
  _globals['_PLUGIN_POINTOPERATION_CREATE']._serialized_end=2103
# @@protoc_insertion_point(module_scope)
