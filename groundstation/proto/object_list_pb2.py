# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='groundstation/proto/object_list.proto',
  package='',
  serialized_pb='\n%groundstation/proto/object_list.proto\" \n\nObjectList\x12\x12\n\nobjectname\x18\x01 \x03(\t')




_OBJECTLIST = descriptor.Descriptor(
  name='ObjectList',
  full_name='ObjectList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='objectname', full_name='ObjectList.objectname', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=41,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['ObjectList'] = _OBJECTLIST

class ObjectList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OBJECTLIST
  
  # @@protoc_insertion_point(class_scope:ObjectList)

# @@protoc_insertion_point(module_scope)