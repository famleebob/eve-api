# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uuid/uuid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='uuid/uuid.proto',
  package='org.lfedge.eve.uuid',
  syntax='proto3',
  serialized_options=_b('\n\023org.lfedge.eve.uuidB\007EveUuidP\001Z\"github.com/lf-edge/eve/api/go/uuid'),
  serialized_pb=_b('\n\x0fuuid/uuid.proto\x12\x13org.lfedge.eve.uuid\"\"\n\x0bUuidRequest\x12\x13\n\x0b\x64\x65vice_cert\x18\x01 \x01(\x0c\"H\n\x0cUuidResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x02 \x01(\t\x12\x14\n\x0cproduct_name\x18\x03 \x01(\tBD\n\x13org.lfedge.eve.uuidB\x07\x45veUuidP\x01Z\"github.com/lf-edge/eve/api/go/uuidb\x06proto3')
)




_UUIDREQUEST = _descriptor.Descriptor(
  name='UuidRequest',
  full_name='org.lfedge.eve.uuid.UuidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_cert', full_name='org.lfedge.eve.uuid.UuidRequest.device_cert', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=74,
)


_UUIDRESPONSE = _descriptor.Descriptor(
  name='UuidResponse',
  full_name='org.lfedge.eve.uuid.UuidResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='org.lfedge.eve.uuid.UuidResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='org.lfedge.eve.uuid.UuidResponse.manufacturer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_name', full_name='org.lfedge.eve.uuid.UuidResponse.product_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['UuidRequest'] = _UUIDREQUEST
DESCRIPTOR.message_types_by_name['UuidResponse'] = _UUIDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UuidRequest = _reflection.GeneratedProtocolMessageType('UuidRequest', (_message.Message,), dict(
  DESCRIPTOR = _UUIDREQUEST,
  __module__ = 'uuid.uuid_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.uuid.UuidRequest)
  ))
_sym_db.RegisterMessage(UuidRequest)

UuidResponse = _reflection.GeneratedProtocolMessageType('UuidResponse', (_message.Message,), dict(
  DESCRIPTOR = _UUIDRESPONSE,
  __module__ = 'uuid.uuid_pb2'
  # @@protoc_insertion_point(class_scope:org.lfedge.eve.uuid.UuidResponse)
  ))
_sym_db.RegisterMessage(UuidResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
