# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"7\n\x08JWTToken\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\"\x15\n\x07Payload\x12\n\n\x02id\x18\x01 \x01(\t2u\n\x0b\x41uthService\x12\x1e\n\x05Login\x12\x08.Payload\x1a\t.JWTToken\"\x00\x12!\n\x07Refresh\x12\t.JWTToken\x1a\t.JWTToken\"\x00\x12#\n\nCheckToken\x12\t.JWTToken\x1a\x08.Payload\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_JWTTOKEN']._serialized_start=14
  _globals['_JWTTOKEN']._serialized_end=69
  _globals['_PAYLOAD']._serialized_start=71
  _globals['_PAYLOAD']._serialized_end=92
  _globals['_AUTHSERVICE']._serialized_start=94
  _globals['_AUTHSERVICE']._serialized_end=211
# @@protoc_insertion_point(module_scope)
