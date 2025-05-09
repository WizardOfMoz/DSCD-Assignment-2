# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: consistency.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='consistency.proto',
  package='consistency',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63onsistency.proto\x12\x0b\x63onsistency\"\x06\n\x04Void\"\x19\n\x06Server\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"$\n\x11ServerRegResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"[\n\x0cWriteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x0b\n\x03seq\x18\x05 \x01(\x03\"M\n\rWriteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x0b\n\x03seq\x18\x04 \x01(\x03\"\x1b\n\x0bReadRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"P\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"=\n\rDeleteRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03seq\x18\x02 \x01(\x03\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"@\n\x0e\x44\x65leteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0b\n\x03seq\x18\x02 \x01(\x03\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x32U\n\x10Server_RegServer\x12\x41\n\x08Register\x12\x13.consistency.Server\x1a\x1e.consistency.ServerRegResponse\"\x00\x32\xcd\x01\n\x10\x43lient_RegServer\x12;\n\rGetServerList\x12\x11.consistency.Void\x1a\x13.consistency.Server\"\x00\x30\x01\x12=\n\x0fGetNWServerList\x12\x11.consistency.Void\x1a\x13.consistency.Server\"\x00\x30\x01\x12=\n\x0fGetNRServerList\x12\x11.consistency.Void\x1a\x13.consistency.Server\"\x00\x30\x01\x32\xd5\x01\n\rClient_Server\x12@\n\x05Write\x12\x19.consistency.WriteRequest\x1a\x1a.consistency.WriteResponse\"\x00\x12=\n\x04Read\x12\x18.consistency.ReadRequest\x1a\x19.consistency.ReadResponse\"\x00\x12\x43\n\x06\x44\x65lete\x12\x1a.consistency.DeleteRequest\x1a\x1b.consistency.DeleteResponse\"\x00\x62\x06proto3')
)




_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='consistency.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=34,
  serialized_end=40,
)


_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='consistency.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='consistency.Server.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=67,
)


_SERVERREGRESPONSE = _descriptor.Descriptor(
  name='ServerRegResponse',
  full_name='consistency.ServerRegResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='consistency.ServerRegResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=69,
  serialized_end=105,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='consistency.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='consistency.WriteRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='consistency.WriteRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='consistency.WriteRequest.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='consistency.WriteRequest.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='consistency.WriteRequest.seq', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=107,
  serialized_end=198,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='consistency.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='consistency.WriteResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='consistency.WriteResponse.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='consistency.WriteResponse.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='consistency.WriteResponse.seq', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=200,
  serialized_end=277,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='consistency.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='consistency.ReadRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=279,
  serialized_end=306,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='consistency.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='consistency.ReadResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='consistency.ReadResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='consistency.ReadResponse.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='consistency.ReadResponse.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=308,
  serialized_end=388,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='consistency.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='consistency.DeleteRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='consistency.DeleteRequest.seq', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='consistency.DeleteRequest.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=390,
  serialized_end=451,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='consistency.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='consistency.DeleteResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='consistency.DeleteResponse.seq', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='consistency.DeleteResponse.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=453,
  serialized_end=517,
)

DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['Server'] = _SERVER
DESCRIPTOR.message_types_by_name['ServerRegResponse'] = _SERVERREGRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.Void)
  ))
_sym_db.RegisterMessage(Void)

Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), dict(
  DESCRIPTOR = _SERVER,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.Server)
  ))
_sym_db.RegisterMessage(Server)

ServerRegResponse = _reflection.GeneratedProtocolMessageType('ServerRegResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREGRESPONSE,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.ServerRegResponse)
  ))
_sym_db.RegisterMessage(ServerRegResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEREQUEST,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.WriteRequest)
  ))
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITERESPONSE,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.WriteResponse)
  ))
_sym_db.RegisterMessage(WriteResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'consistency_pb2'
  # @@protoc_insertion_point(class_scope:consistency.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)



_SERVER_REGSERVER = _descriptor.ServiceDescriptor(
  name='Server_RegServer',
  full_name='consistency.Server_RegServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=519,
  serialized_end=604,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='consistency.Server_RegServer.Register',
    index=0,
    containing_service=None,
    input_type=_SERVER,
    output_type=_SERVERREGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER_REGSERVER)

DESCRIPTOR.services_by_name['Server_RegServer'] = _SERVER_REGSERVER


_CLIENT_REGSERVER = _descriptor.ServiceDescriptor(
  name='Client_RegServer',
  full_name='consistency.Client_RegServer',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=607,
  serialized_end=812,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerList',
    full_name='consistency.Client_RegServer.GetServerList',
    index=0,
    containing_service=None,
    input_type=_VOID,
    output_type=_SERVER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNWServerList',
    full_name='consistency.Client_RegServer.GetNWServerList',
    index=1,
    containing_service=None,
    input_type=_VOID,
    output_type=_SERVER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNRServerList',
    full_name='consistency.Client_RegServer.GetNRServerList',
    index=2,
    containing_service=None,
    input_type=_VOID,
    output_type=_SERVER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENT_REGSERVER)

DESCRIPTOR.services_by_name['Client_RegServer'] = _CLIENT_REGSERVER


_CLIENT_SERVER = _descriptor.ServiceDescriptor(
  name='Client_Server',
  full_name='consistency.Client_Server',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=815,
  serialized_end=1028,
  methods=[
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='consistency.Client_Server.Write',
    index=0,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='consistency.Client_Server.Read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='consistency.Client_Server.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENT_SERVER)

DESCRIPTOR.services_by_name['Client_Server'] = _CLIENT_SERVER

# @@protoc_insertion_point(module_scope)
