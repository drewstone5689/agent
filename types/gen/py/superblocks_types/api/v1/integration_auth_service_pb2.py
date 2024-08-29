# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1/integration_auth_service.proto
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
    'api/v1/integration_auth_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from superblocks_types.buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from superblocks_types.common.v1 import common_pb2 as common_dot_v1_dot_common__pb2
from superblocks_types.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from superblocks_types.plugins.common.v1 import auth_pb2 as plugins_dot_common_dot_v1_dot_auth__pb2
from superblocks_types.protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from superblocks_types.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1/integration_auth_service.proto\x12\x06\x61pi.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x16\x63ommon/v1/common.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cplugins/common/v1/auth.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x17validate/validate.proto\"y\n\x10\x43heckAuthRequest\x12\x37\n\x0eintegration_id\x18\x01 \x01(\tB\x10\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\rintegrationId\x12,\n\x07profile\x18\x02 \x01(\x0b\x32\x12.common.v1.ProfileR\x07profile\"9\n\x11\x43heckAuthResponse\x12$\n\rauthenticated\x18\x01 \x01(\x08R\rauthenticated\"\xc2\x02\n\x0cLoginRequest\x12\x37\n\x0eintegration_id\x18\x01 \x01(\tB\x10\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\rintegrationId\x12,\n\x07profile\x18\x02 \x01(\x0b\x32\x12.common.v1.ProfileR\x07profile\x12\x19\n\x05token\x18\x03 \x01(\tH\x00R\x05token\x88\x01\x01\x12\'\n\x0crefreshToken\x18\x04 \x01(\tH\x01R\x0crefreshToken\x88\x01\x01\x12\x1d\n\x07idToken\x18\x05 \x01(\tH\x02R\x07idToken\x88\x01\x01\x12-\n\x0f\x65xpiryTimestamp\x18\x06 \x01(\x03H\x03R\x0f\x65xpiryTimestamp\x88\x01\x01\x42\x08\n\x06_tokenB\x0f\n\r_refreshTokenB\n\n\x08_idTokenB\x12\n\x10_expiryTimestamp\")\n\rLoginResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\"\xd7\x02\n ExchangeOauthCodeForTokenRequest\x12\x39\n\x0eintegration_id\x18\x01 \x01(\tB\x12\x18\x01\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\rintegrationId\x12,\n\x07profile\x18\x02 \x01(\x0b\x32\x12.common.v1.ProfileR\x07profile\x12\x1f\n\x0b\x61\x63\x63\x65ss_code\x18\x03 \x01(\tR\naccessCode\x12\x1b\n\tauth_type\x18\x04 \x01(\tR\x08\x61uthType\x12O\n\x0b\x61uth_config\x18\x05 \x01(\x0b\x32..plugins.common.v1.OAuth.AuthorizationCodeFlowR\nauthConfig\x12;\n\x10\x63onfiguration_id\x18\x06 \x01(\tB\x10\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\x0f\x63onfigurationId\"\xc1\x01\n RequestOauthPasswordTokenRequest\x12\x37\n\x0eintegration_id\x18\x01 \x01(\tB\x10\xfa\x42\x05r\x03\xb0\x01\x01\xbaH\x05r\x03\xb0\x01\x01R\rintegrationId\x12,\n\x07profile\x18\x02 \x01(\x0b\x32\x12.common.v1.ProfileR\x07profile\x12\x1a\n\x08username\x18\x03 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x04 \x01(\tR\x08password\"\x96\x01\n!RequestOauthPasswordTokenResponse\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12#\n\rrefresh_token\x18\x02 \x01(\tR\x0crefreshToken\x12)\n\x10\x65xpiry_timestamp\x18\x03 \x01(\x03R\x0f\x65xpiryTimestamp2\xf4\x04\n\x16IntegrationAuthService\x12i\n\tCheckAuth\x12\x18.api.v1.CheckAuthRequest\x1a\x19.api.v1.CheckAuthResponse\"\'\x92\x41\x0b*\tCheckAuth\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/check-auth:\x01*\x12T\n\x05Login\x12\x14.api.v1.LoginRequest\x1a\x15.api.v1.LoginResponse\"\x1e\x92\x41\x07*\x05Login\x82\xd3\xe4\x93\x02\x0e\"\t/v1/login:\x01*\x12Z\n\x06Logout\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\" \x92\x41\x08*\x06Logout\x82\xd3\xe4\x93\x02\x0f\"\n/v1/logout:\x01*\x12\x99\x01\n\x19\x45xchangeOauthCodeForToken\x12(.api.v1.ExchangeOauthCodeForTokenRequest\x1a\x16.google.protobuf.Empty\":\x92\x41\x1b*\x19\x45xchangeOauthCodeForToken\x82\xd3\xe4\x93\x02\x16\"\x11/v1/exchange-code:\x01*\x12\xa0\x01\n\x19RequestOauthPasswordToken\x12(.api.v1.RequestOauthPasswordTokenRequest\x1a).api.v1.RequestOauthPasswordTokenResponse\".\x92\x41\x0f*\rRequest Token\x82\xd3\xe4\x93\x02\x16\"\x11/v1/request-token:\x01*B6Z4github.com/superblocksteam/agent/types/gen/go/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1.integration_auth_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/superblocksteam/agent/types/gen/go/api/v1'
  _globals['_CHECKAUTHREQUEST'].fields_by_name['integration_id']._loaded_options = None
  _globals['_CHECKAUTHREQUEST'].fields_by_name['integration_id']._serialized_options = b'\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_LOGINREQUEST'].fields_by_name['integration_id']._loaded_options = None
  _globals['_LOGINREQUEST'].fields_by_name['integration_id']._serialized_options = b'\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST'].fields_by_name['integration_id']._loaded_options = None
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST'].fields_by_name['integration_id']._serialized_options = b'\030\001\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST'].fields_by_name['configuration_id']._loaded_options = None
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST'].fields_by_name['configuration_id']._serialized_options = b'\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_REQUESTOAUTHPASSWORDTOKENREQUEST'].fields_by_name['integration_id']._loaded_options = None
  _globals['_REQUESTOAUTHPASSWORDTOKENREQUEST'].fields_by_name['integration_id']._serialized_options = b'\372B\005r\003\260\001\001\272H\005r\003\260\001\001'
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['CheckAuth']._loaded_options = None
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['CheckAuth']._serialized_options = b'\222A\013*\tCheckAuth\202\323\344\223\002\023\"\016/v1/check-auth:\001*'
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['Login']._loaded_options = None
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['Login']._serialized_options = b'\222A\007*\005Login\202\323\344\223\002\016\"\t/v1/login:\001*'
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['Logout']._loaded_options = None
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['Logout']._serialized_options = b'\222A\010*\006Logout\202\323\344\223\002\017\"\n/v1/logout:\001*'
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['ExchangeOauthCodeForToken']._loaded_options = None
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['ExchangeOauthCodeForToken']._serialized_options = b'\222A\033*\031ExchangeOauthCodeForToken\202\323\344\223\002\026\"\021/v1/exchange-code:\001*'
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['RequestOauthPasswordToken']._loaded_options = None
  _globals['_INTEGRATIONAUTHSERVICE'].methods_by_name['RequestOauthPasswordToken']._serialized_options = b'\222A\017*\rRequest Token\202\323\344\223\002\026\"\021/v1/request-token:\001*'
  _globals['_CHECKAUTHREQUEST']._serialized_start=264
  _globals['_CHECKAUTHREQUEST']._serialized_end=385
  _globals['_CHECKAUTHRESPONSE']._serialized_start=387
  _globals['_CHECKAUTHRESPONSE']._serialized_end=444
  _globals['_LOGINREQUEST']._serialized_start=447
  _globals['_LOGINREQUEST']._serialized_end=769
  _globals['_LOGINRESPONSE']._serialized_start=771
  _globals['_LOGINRESPONSE']._serialized_end=812
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST']._serialized_start=815
  _globals['_EXCHANGEOAUTHCODEFORTOKENREQUEST']._serialized_end=1158
  _globals['_REQUESTOAUTHPASSWORDTOKENREQUEST']._serialized_start=1161
  _globals['_REQUESTOAUTHPASSWORDTOKENREQUEST']._serialized_end=1354
  _globals['_REQUESTOAUTHPASSWORDTOKENRESPONSE']._serialized_start=1357
  _globals['_REQUESTOAUTHPASSWORDTOKENRESPONSE']._serialized_end=1507
  _globals['_INTEGRATIONAUTHSERVICE']._serialized_start=1510
  _globals['_INTEGRATIONAUTHSERVICE']._serialized_end=2138
# @@protoc_insertion_point(module_scope)
