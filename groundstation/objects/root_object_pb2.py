# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groundstation/objects/root_object.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='groundstation/objects/root_object.proto',
  package='',
  serialized_pb='\n\'groundstation/objects/root_object.proto\";\n\nRootObject\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0f\n\x07\x63hannel\x18\x02 \x02(\t\x12\x10\n\x08protocol\x18\x03 \x02(\t')




_ROOTOBJECT = _descriptor.Descriptor(
  name='RootObject',
  full_name='RootObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RootObject.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='RootObject.channel', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='RootObject.protocol', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=43,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['RootObject'] = _ROOTOBJECT

class RootObject(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROOTOBJECT

  # @@protoc_insertion_point(class_scope:RootObject)


# @@protoc_insertion_point(module_scope)
