# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fleetspeak/src/client/proto/fleetspeak_client/api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fleetspeak/src/client/proto/fleetspeak_client/api.proto',
  package='fleetspeak.client',
  syntax='proto3',
  serialized_pb=_b('\n7fleetspeak/src/client/proto/fleetspeak_client/api.proto\x12\x11\x66leetspeak.client\x1a\x19google/protobuf/any.proto\"\x18\n\x08\x42yteBlob\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\">\n\nAPIMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_BYTEBLOB = _descriptor.Descriptor(
  name='ByteBlob',
  full_name='fleetspeak.client.ByteBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='fleetspeak.client.ByteBlob.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=129,
)


_APIMESSAGE = _descriptor.Descriptor(
  name='APIMessage',
  full_name='fleetspeak.client.APIMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='fleetspeak.client.APIMessage.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='fleetspeak.client.APIMessage.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=193,
)

_APIMESSAGE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['ByteBlob'] = _BYTEBLOB
DESCRIPTOR.message_types_by_name['APIMessage'] = _APIMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ByteBlob = _reflection.GeneratedProtocolMessageType('ByteBlob', (_message.Message,), dict(
  DESCRIPTOR = _BYTEBLOB,
  __module__ = 'fleetspeak.src.client.proto.fleetspeak_client.api_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.client.ByteBlob)
  ))
_sym_db.RegisterMessage(ByteBlob)

APIMessage = _reflection.GeneratedProtocolMessageType('APIMessage', (_message.Message,), dict(
  DESCRIPTOR = _APIMESSAGE,
  __module__ = 'fleetspeak.src.client.proto.fleetspeak_client.api_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.client.APIMessage)
  ))
_sym_db.RegisterMessage(APIMessage)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
