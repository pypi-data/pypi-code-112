# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/reader_base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/reader_base.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\020ReaderBaseProtosP\001ZRgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/reader_base_go_proto\370\001\001'),
  serialized_pb=_b('\n+tensorflow/core/framework/reader_base.proto\x12\ntensorflow\"r\n\x0fReaderBaseState\x12\x14\n\x0cwork_started\x18\x01 \x01(\x03\x12\x15\n\rwork_finished\x18\x02 \x01(\x03\x12\x1c\n\x14num_records_produced\x18\x03 \x01(\x03\x12\x14\n\x0c\x63urrent_work\x18\x04 \x01(\x0c\x42\x85\x01\n\x18org.tensorflow.frameworkB\x10ReaderBaseProtosP\x01ZRgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/reader_base_go_proto\xf8\x01\x01\x62\x06proto3')
)




_READERBASESTATE = _descriptor.Descriptor(
  name='ReaderBaseState',
  full_name='tensorflow.ReaderBaseState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_started', full_name='tensorflow.ReaderBaseState.work_started', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_finished', full_name='tensorflow.ReaderBaseState.work_finished', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_records_produced', full_name='tensorflow.ReaderBaseState.num_records_produced', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_work', full_name='tensorflow.ReaderBaseState.current_work', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['ReaderBaseState'] = _READERBASESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReaderBaseState = _reflection.GeneratedProtocolMessageType('ReaderBaseState', (_message.Message,), {
  'DESCRIPTOR' : _READERBASESTATE,
  '__module__' : 'tensorflow.core.framework.reader_base_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ReaderBaseState)
  })
_sym_db.RegisterMessage(ReaderBaseState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
