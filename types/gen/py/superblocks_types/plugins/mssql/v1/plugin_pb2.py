# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: plugins/mssql/v1/plugin.proto
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
    'plugins/mssql/v1/plugin.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dplugins/mssql/v1/plugin.proto\x12\x10plugins.mssql.v1\x1a\x19google/protobuf/any.proto\"5\n\rMappedColumns\x12\x12\n\x04json\x18\x01 \x01(\tR\x04json\x12\x10\n\x03sql\x18\x02 \x01(\tR\x03sql\"E\n\x05Tuple\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyR\x05value\";\n\x13SuperblocksMetadata\x12$\n\rpluginVersion\x18\x01 \x01(\tR\rpluginVersion\"\xd7\x05\n\x06Plugin\x12\x12\n\x04\x62ody\x18\x01 \x01(\tR\x04\x62ody\x12&\n\x0eusePreparedSql\x18\x02 \x01(\x08R\x0eusePreparedSql\x12!\n\toperation\x18\x03 \x01(\tH\x00R\toperation\x88\x01\x01\x12\x35\n\x13useAdvancedMatching\x18\x04 \x01(\tH\x01R\x13useAdvancedMatching\x88\x01\x01\x12\x19\n\x05table\x18\x05 \x01(\tH\x02R\x05table\x88\x01\x01\x12!\n\tnewValues\x18\x06 \x01(\tH\x03R\tnewValues\x88\x01\x01\x12!\n\toldValues\x18\x07 \x01(\tH\x04R\toldValues\x88\x01\x01\x12\x1a\n\x08\x66ilterBy\x18\x08 \x03(\tR\x08\x66ilterBy\x12%\n\x0bmappingMode\x18\t \x01(\tH\x05R\x0bmappingMode\x88\x01\x01\x12\x45\n\rmappedColumns\x18\n \x03(\x0b\x32\x1f.plugins.mssql.v1.MappedColumnsR\rmappedColumns\x12W\n\x13superblocksMetadata\x18\x0b \x01(\x0b\x32%.plugins.mssql.v1.SuperblocksMetadataR\x13superblocksMetadata\x12\'\n\x0cinsertedRows\x18\x0c \x01(\tH\x06R\x0cinsertedRows\x88\x01\x01\x12%\n\x0b\x64\x65letedRows\x18\r \x01(\tH\x07R\x0b\x64\x65letedRows\x88\x01\x01\x12\x1b\n\x06schema\x18\x0e \x01(\tH\x08R\x06schema\x88\x01\x01\x42\x0c\n\n_operationB\x16\n\x14_useAdvancedMatchingB\x08\n\x06_tableB\x0c\n\n_newValuesB\x0c\n\n_oldValuesB\x0e\n\x0c_mappingModeB\x0f\n\r_insertedRowsB\x0e\n\x0c_deletedRowsB\t\n\x07_schemaB@Z>github.com/superblocksteam/agent/types/gen/go/plugins/mssql/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugins.mssql.v1.plugin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/superblocksteam/agent/types/gen/go/plugins/mssql/v1'
  _globals['_MAPPEDCOLUMNS']._serialized_start=78
  _globals['_MAPPEDCOLUMNS']._serialized_end=131
  _globals['_TUPLE']._serialized_start=133
  _globals['_TUPLE']._serialized_end=202
  _globals['_SUPERBLOCKSMETADATA']._serialized_start=204
  _globals['_SUPERBLOCKSMETADATA']._serialized_end=263
  _globals['_PLUGIN']._serialized_start=266
  _globals['_PLUGIN']._serialized_end=993
# @@protoc_insertion_point(module_scope)
