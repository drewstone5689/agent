// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.32.0
// 	protoc        (unknown)
// source: common/v1/errors.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Code int32

const (
	Code_CODE_UNSPECIFIED                        Code = 0
	Code_CODE_INTEGRATION_AUTHORIZATION          Code = 1
	Code_CODE_INTEGRATION_NETWORK                Code = 2
	Code_CODE_INTEGRATION_QUERY_TIMEOUT          Code = 3
	Code_CODE_INTEGRATION_SYNTAX                 Code = 4
	Code_CODE_INTEGRATION_LOGIC                  Code = 5
	Code_CODE_INTEGRATION_MISSING_REQUIRED_FIELD Code = 6
	Code_CODE_INTEGRATION_RATE_LIMIT             Code = 7
	Code_CODE_INTEGRATION_USER_CANCELLED         Code = 8
	Code_CODE_INTEGRATION_INTERNAL               Code = 9
)

// Enum value maps for Code.
var (
	Code_name = map[int32]string{
		0: "CODE_UNSPECIFIED",
		1: "CODE_INTEGRATION_AUTHORIZATION",
		2: "CODE_INTEGRATION_NETWORK",
		3: "CODE_INTEGRATION_QUERY_TIMEOUT",
		4: "CODE_INTEGRATION_SYNTAX",
		5: "CODE_INTEGRATION_LOGIC",
		6: "CODE_INTEGRATION_MISSING_REQUIRED_FIELD",
		7: "CODE_INTEGRATION_RATE_LIMIT",
		8: "CODE_INTEGRATION_USER_CANCELLED",
		9: "CODE_INTEGRATION_INTERNAL",
	}
	Code_value = map[string]int32{
		"CODE_UNSPECIFIED":                        0,
		"CODE_INTEGRATION_AUTHORIZATION":          1,
		"CODE_INTEGRATION_NETWORK":                2,
		"CODE_INTEGRATION_QUERY_TIMEOUT":          3,
		"CODE_INTEGRATION_SYNTAX":                 4,
		"CODE_INTEGRATION_LOGIC":                  5,
		"CODE_INTEGRATION_MISSING_REQUIRED_FIELD": 6,
		"CODE_INTEGRATION_RATE_LIMIT":             7,
		"CODE_INTEGRATION_USER_CANCELLED":         8,
		"CODE_INTEGRATION_INTERNAL":               9,
	}
)

func (x Code) Enum() *Code {
	p := new(Code)
	*p = x
	return p
}

func (x Code) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Code) Descriptor() protoreflect.EnumDescriptor {
	return file_common_v1_errors_proto_enumTypes[0].Descriptor()
}

func (Code) Type() protoreflect.EnumType {
	return &file_common_v1_errors_proto_enumTypes[0]
}

func (x Code) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Code.Descriptor instead.
func (Code) EnumDescriptor() ([]byte, []int) {
	return file_common_v1_errors_proto_rawDescGZIP(), []int{0}
}

type Error struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name      string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Message   string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
	Handled   bool   `protobuf:"varint,3,opt,name=handled,proto3" json:"handled,omitempty"`
	BlockPath string `protobuf:"bytes,4,opt,name=block_path,json=blockPath,proto3" json:"block_path,omitempty"`
	FormPath  string `protobuf:"bytes,5,opt,name=form_path,json=formPath,proto3" json:"form_path,omitempty"`
	Code      Code   `protobuf:"varint,6,opt,name=code,proto3,enum=common.v1.Code" json:"code,omitempty"`
}

func (x *Error) Reset() {
	*x = Error{}
	if protoimpl.UnsafeEnabled {
		mi := &file_common_v1_errors_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Error) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Error) ProtoMessage() {}

func (x *Error) ProtoReflect() protoreflect.Message {
	mi := &file_common_v1_errors_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Error.ProtoReflect.Descriptor instead.
func (*Error) Descriptor() ([]byte, []int) {
	return file_common_v1_errors_proto_rawDescGZIP(), []int{0}
}

func (x *Error) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *Error) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

func (x *Error) GetHandled() bool {
	if x != nil {
		return x.Handled
	}
	return false
}

func (x *Error) GetBlockPath() string {
	if x != nil {
		return x.BlockPath
	}
	return ""
}

func (x *Error) GetFormPath() string {
	if x != nil {
		return x.FormPath
	}
	return ""
}

func (x *Error) GetCode() Code {
	if x != nil {
		return x.Code
	}
	return Code_CODE_UNSPECIFIED
}

var File_common_v1_errors_proto protoreflect.FileDescriptor

var file_common_v1_errors_proto_rawDesc = []byte{
	0x0a, 0x16, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x65, 0x72, 0x72, 0x6f,
	0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x09, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e,
	0x2e, 0x76, 0x31, 0x22, 0xb0, 0x01, 0x0a, 0x05, 0x45, 0x72, 0x72, 0x6f, 0x72, 0x12, 0x12, 0x0a,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x68,
	0x61, 0x6e, 0x64, 0x6c, 0x65, 0x64, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x07, 0x68, 0x61,
	0x6e, 0x64, 0x6c, 0x65, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x62, 0x6c, 0x6f, 0x63, 0x6b, 0x5f, 0x70,
	0x61, 0x74, 0x68, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x62, 0x6c, 0x6f, 0x63, 0x6b,
	0x50, 0x61, 0x74, 0x68, 0x12, 0x1b, 0x0a, 0x09, 0x66, 0x6f, 0x72, 0x6d, 0x5f, 0x70, 0x61, 0x74,
	0x68, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x66, 0x6f, 0x72, 0x6d, 0x50, 0x61, 0x74,
	0x68, 0x12, 0x23, 0x0a, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0e, 0x32,
	0x0f, 0x2e, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x6f, 0x64, 0x65,
	0x52, 0x04, 0x63, 0x6f, 0x64, 0x65, 0x2a, 0xcd, 0x02, 0x0a, 0x04, 0x43, 0x6f, 0x64, 0x65, 0x12,
	0x14, 0x0a, 0x10, 0x43, 0x4f, 0x44, 0x45, 0x5f, 0x55, 0x4e, 0x53, 0x50, 0x45, 0x43, 0x49, 0x46,
	0x49, 0x45, 0x44, 0x10, 0x00, 0x12, 0x22, 0x0a, 0x1e, 0x43, 0x4f, 0x44, 0x45, 0x5f, 0x49, 0x4e,
	0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x41, 0x55, 0x54, 0x48, 0x4f, 0x52,
	0x49, 0x5a, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x10, 0x01, 0x12, 0x1c, 0x0a, 0x18, 0x43, 0x4f, 0x44,
	0x45, 0x5f, 0x49, 0x4e, 0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x4e, 0x45,
	0x54, 0x57, 0x4f, 0x52, 0x4b, 0x10, 0x02, 0x12, 0x22, 0x0a, 0x1e, 0x43, 0x4f, 0x44, 0x45, 0x5f,
	0x49, 0x4e, 0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x51, 0x55, 0x45, 0x52,
	0x59, 0x5f, 0x54, 0x49, 0x4d, 0x45, 0x4f, 0x55, 0x54, 0x10, 0x03, 0x12, 0x1b, 0x0a, 0x17, 0x43,
	0x4f, 0x44, 0x45, 0x5f, 0x49, 0x4e, 0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f,
	0x53, 0x59, 0x4e, 0x54, 0x41, 0x58, 0x10, 0x04, 0x12, 0x1a, 0x0a, 0x16, 0x43, 0x4f, 0x44, 0x45,
	0x5f, 0x49, 0x4e, 0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x4c, 0x4f, 0x47,
	0x49, 0x43, 0x10, 0x05, 0x12, 0x2b, 0x0a, 0x27, 0x43, 0x4f, 0x44, 0x45, 0x5f, 0x49, 0x4e, 0x54,
	0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x4d, 0x49, 0x53, 0x53, 0x49, 0x4e, 0x47,
	0x5f, 0x52, 0x45, 0x51, 0x55, 0x49, 0x52, 0x45, 0x44, 0x5f, 0x46, 0x49, 0x45, 0x4c, 0x44, 0x10,
	0x06, 0x12, 0x1f, 0x0a, 0x1b, 0x43, 0x4f, 0x44, 0x45, 0x5f, 0x49, 0x4e, 0x54, 0x45, 0x47, 0x52,
	0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x52, 0x41, 0x54, 0x45, 0x5f, 0x4c, 0x49, 0x4d, 0x49, 0x54,
	0x10, 0x07, 0x12, 0x23, 0x0a, 0x1f, 0x43, 0x4f, 0x44, 0x45, 0x5f, 0x49, 0x4e, 0x54, 0x45, 0x47,
	0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x55, 0x53, 0x45, 0x52, 0x5f, 0x43, 0x41, 0x4e, 0x43,
	0x45, 0x4c, 0x4c, 0x45, 0x44, 0x10, 0x08, 0x12, 0x1d, 0x0a, 0x19, 0x43, 0x4f, 0x44, 0x45, 0x5f,
	0x49, 0x4e, 0x54, 0x45, 0x47, 0x52, 0x41, 0x54, 0x49, 0x4f, 0x4e, 0x5f, 0x49, 0x4e, 0x54, 0x45,
	0x52, 0x4e, 0x41, 0x4c, 0x10, 0x09, 0x42, 0x39, 0x5a, 0x37, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62,
	0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x75, 0x70, 0x65, 0x72, 0x62, 0x6c, 0x6f, 0x63, 0x6b, 0x73,
	0x74, 0x65, 0x61, 0x6d, 0x2f, 0x61, 0x67, 0x65, 0x6e, 0x74, 0x2f, 0x74, 0x79, 0x70, 0x65, 0x73,
	0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x67, 0x6f, 0x2f, 0x63, 0x6f, 0x6d, 0x6d, 0x6f, 0x6e, 0x2f, 0x76,
	0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_common_v1_errors_proto_rawDescOnce sync.Once
	file_common_v1_errors_proto_rawDescData = file_common_v1_errors_proto_rawDesc
)

func file_common_v1_errors_proto_rawDescGZIP() []byte {
	file_common_v1_errors_proto_rawDescOnce.Do(func() {
		file_common_v1_errors_proto_rawDescData = protoimpl.X.CompressGZIP(file_common_v1_errors_proto_rawDescData)
	})
	return file_common_v1_errors_proto_rawDescData
}

var file_common_v1_errors_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_common_v1_errors_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_common_v1_errors_proto_goTypes = []interface{}{
	(Code)(0),     // 0: common.v1.Code
	(*Error)(nil), // 1: common.v1.Error
}
var file_common_v1_errors_proto_depIdxs = []int32{
	0, // 0: common.v1.Error.code:type_name -> common.v1.Code
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_common_v1_errors_proto_init() }
func file_common_v1_errors_proto_init() {
	if File_common_v1_errors_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_common_v1_errors_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Error); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_common_v1_errors_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_common_v1_errors_proto_goTypes,
		DependencyIndexes: file_common_v1_errors_proto_depIdxs,
		EnumInfos:         file_common_v1_errors_proto_enumTypes,
		MessageInfos:      file_common_v1_errors_proto_msgTypes,
	}.Build()
	File_common_v1_errors_proto = out.File
	file_common_v1_errors_proto_rawDesc = nil
	file_common_v1_errors_proto_goTypes = nil
	file_common_v1_errors_proto_depIdxs = nil
}
