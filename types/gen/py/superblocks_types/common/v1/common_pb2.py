# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/v1/common.proto
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
    'common/v1/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from superblocks_types.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63ommon/v1/common.proto\x12\tcommon.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\"\xb6\x01\n\nTimestamps\x12\x34\n\x07\x63reated\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x34\n\x07updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07updated\x12<\n\x0b\x64\x65\x61\x63tivated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x65\x61\x63tivated\"\xc3\x03\n\x08Metadata\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00R\x0b\x64\x65scription\x88\x01\x01\x12\"\n\x04name\x18\x03 \x01(\tB\x0e\xfa\x42\x04r\x02\x10\x01\xbaH\x04r\x02\x10\x01R\x04name\x12\x34\n\x0corganization\x18\x04 \x01(\tB\x10\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\x0corganization\x12\x1b\n\x06\x66older\x18\x05 \x01(\tH\x01R\x06\x66older\x88\x01\x01\x12\x35\n\ntimestamps\x18\x06 \x01(\x0b\x32\x15.common.v1.TimestampsR\ntimestamps\x12\x1d\n\x07version\x18\x07 \x01(\tH\x02R\x07version\x88\x01\x01\x12\x31\n\x04tags\x18\x08 \x03(\x0b\x32\x1d.common.v1.Metadata.TagsEntryR\x04tags\x12\x17\n\x04type\x18\t \x01(\tH\x03R\x04type\x88\x01\x01\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x0e\n\x0c_descriptionB\t\n\x07_folderB\n\n\x08_versionB\x07\n\x05_type\"~\n\x07Profile\x12\x13\n\x02id\x18\x01 \x01(\tH\x00R\x02id\x88\x01\x01\x12\x17\n\x04name\x18\x02 \x01(\tH\x01R\x04name\x88\x01\x01\x12%\n\x0b\x65nvironment\x18\x03 \x01(\tH\x02R\x0b\x65nvironment\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_nameB\x0e\n\x0c_environment*X\n\x08UserType\x12\x19\n\x15USER_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15USER_TYPE_SUPERBLOCKS\x10\x01\x12\x16\n\x12USER_TYPE_EXTERNAL\x10\x02\x42\x39Z7github.com/superblocksteam/agent/types/gen/go/common/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/superblocksteam/agent/types/gen/go/common/v1'
  _globals['_METADATA_TAGSENTRY']._loaded_options = None
  _globals['_METADATA_TAGSENTRY']._serialized_options = b'8\001'
  _globals['_METADATA'].fields_by_name['name']._loaded_options = None
  _globals['_METADATA'].fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001\272H\004r\002\020\001'
  _globals['_METADATA'].fields_by_name['organization']._loaded_options = None
  _globals['_METADATA'].fields_by_name['organization']._serialized_options = b'\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_USERTYPE']._serialized_start=891
  _globals['_USERTYPE']._serialized_end=979
  _globals['_TIMESTAMPS']._serialized_start=125
  _globals['_TIMESTAMPS']._serialized_end=307
  _globals['_METADATA']._serialized_start=310
  _globals['_METADATA']._serialized_end=761
  _globals['_METADATA_TAGSENTRY']._serialized_start=658
  _globals['_METADATA_TAGSENTRY']._serialized_end=713
  _globals['_PROFILE']._serialized_start=763
  _globals['_PROFILE']._serialized_end=889
# @@protoc_insertion_point(module_scope)
