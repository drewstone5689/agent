# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plugins/adls/v1/plugin.proto
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
    'plugins/adls/v1/plugin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.plugins.common.v1 import auth_pb2 as plugins_dot_common_dot_v1_dot_auth__pb2
from superblocks_types.plugins.common.v1 import plugin_pb2 as plugins_dot_common_dot_v1_dot_plugin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cplugins/adls/v1/plugin.proto\x12\x0fplugins.adls.v1\x1a\x1cplugins/common/v1/auth.proto\x1a\x1eplugins/common/v1/plugin.proto\"\xc0\r\n\x06Plugin\x12\x17\n\x04name\x18\x01 \x01(\tH\x01R\x04name\x88\x01\x01\x12z\n\x1e\x64ynamic_workflow_configuration\x18\x02 \x01(\x0b\x32/.plugins.common.v1.DynamicWorkflowConfigurationH\x02R\x1c\x64ynamicWorkflowConfiguration\x88\x01\x01\x12\x46\n\nconnection\x18\x03 \x01(\x0b\x32&.plugins.adls.v1.Plugin.AdlsConnectionR\nconnection\x12T\n\x10\x63reate_container\x18\x04 \x01(\x0b\x32\'.plugins.adls.v1.Plugin.CreateContainerH\x00R\x0f\x63reateContainer\x12T\n\x10\x63reate_directory\x18\x05 \x01(\x0b\x32\'.plugins.adls.v1.Plugin.CreateDirectoryH\x00R\x0f\x63reateDirectory\x12T\n\x10rename_directory\x18\x06 \x01(\x0b\x32\'.plugins.adls.v1.Plugin.RenameDirectoryH\x00R\x0frenameDirectory\x12T\n\x10\x64\x65lete_directory\x18\x07 \x01(\x0b\x32\'.plugins.adls.v1.Plugin.DeleteDirectoryH\x00R\x0f\x64\x65leteDirectory\x12g\n\x17list_directory_contents\x18\x08 \x01(\x0b\x32-.plugins.adls.v1.Plugin.ListDirectoryContentsH\x00R\x15listDirectoryContents\x12\x45\n\x0bupload_file\x18\t \x01(\x0b\x32\".plugins.adls.v1.Plugin.UploadFileH\x00R\nuploadFile\x12K\n\rdownload_file\x18\n \x01(\x0b\x32$.plugins.adls.v1.Plugin.DownloadFileH\x00R\x0c\x64ownloadFile\x12\x45\n\x0b\x64\x65lete_file\x18\x0b \x01(\x0b\x32\".plugins.adls.v1.Plugin.DeleteFileH\x00R\ndeleteFile\x1ay\n\x0e\x41\x64lsConnection\x12!\n\x0c\x61\x63\x63ount_name\x18\x01 \x01(\tR\x0b\x61\x63\x63ountName\x12\x16\n\x06tenant\x18\x02 \x01(\tR\x06tenant\x12,\n\x04\x61uth\x18\x03 \x01(\x0b\x32\x18.plugins.common.v1.AzureR\x04\x61uth\x1a\x32\n\x0f\x43reateContainer\x12\x1f\n\x0b\x66ile_system\x18\x02 \x01(\tR\nfileSystem\x1a\x46\n\x0f\x43reateDirectory\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x1a\x61\n\x0fRenameDirectory\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x19\n\x08new_path\x18\x03 \x01(\tR\x07newPath\x1a\x46\n\x0f\x44\x65leteDirectory\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x1aL\n\x15ListDirectoryContents\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x1a[\n\nUploadFile\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x12\x18\n\x07\x63ontent\x18\x03 \x01(\tR\x07\x63ontent\x1a\x43\n\x0c\x44ownloadFile\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x1a\x41\n\nDeleteFile\x12\x1f\n\x0b\x66ile_system\x18\x01 \x01(\tR\nfileSystem\x12\x12\n\x04path\x18\x02 \x01(\tR\x04path\x1a-\n\x08Metadata\x12!\n\x0c\x66ile_systems\x18\x01 \x03(\tR\x0b\x66ileSystemsB\r\n\x0b\x61\x64ls_actionB\x07\n\x05_nameB!\n\x1f_dynamic_workflow_configurationB?Z=github.com/superblocksteam/agent/types/gen/go/plugins/adls/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.adls.v1.plugin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/superblocksteam/agent/types/gen/go/plugins/adls/v1'
  _globals['_PLUGIN']._serialized_start=112
  _globals['_PLUGIN']._serialized_end=1840
  _globals['_PLUGIN_ADLSCONNECTION']._serialized_start=1011
  _globals['_PLUGIN_ADLSCONNECTION']._serialized_end=1132
  _globals['_PLUGIN_CREATECONTAINER']._serialized_start=1134
  _globals['_PLUGIN_CREATECONTAINER']._serialized_end=1184
  _globals['_PLUGIN_CREATEDIRECTORY']._serialized_start=1186
  _globals['_PLUGIN_CREATEDIRECTORY']._serialized_end=1256
  _globals['_PLUGIN_RENAMEDIRECTORY']._serialized_start=1258
  _globals['_PLUGIN_RENAMEDIRECTORY']._serialized_end=1355
  _globals['_PLUGIN_DELETEDIRECTORY']._serialized_start=1357
  _globals['_PLUGIN_DELETEDIRECTORY']._serialized_end=1427
  _globals['_PLUGIN_LISTDIRECTORYCONTENTS']._serialized_start=1429
  _globals['_PLUGIN_LISTDIRECTORYCONTENTS']._serialized_end=1505
  _globals['_PLUGIN_UPLOADFILE']._serialized_start=1507
  _globals['_PLUGIN_UPLOADFILE']._serialized_end=1598
  _globals['_PLUGIN_DOWNLOADFILE']._serialized_start=1600
  _globals['_PLUGIN_DOWNLOADFILE']._serialized_end=1667
  _globals['_PLUGIN_DELETEFILE']._serialized_start=1669
  _globals['_PLUGIN_DELETEFILE']._serialized_end=1734
  _globals['_PLUGIN_METADATA']._serialized_start=1736
  _globals['_PLUGIN_METADATA']._serialized_end=1781
# @@protoc_insertion_point(module_scope)
