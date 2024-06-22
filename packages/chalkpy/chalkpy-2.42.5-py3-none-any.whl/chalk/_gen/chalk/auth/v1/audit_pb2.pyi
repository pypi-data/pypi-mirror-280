from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

AUDIT_FIELD_NUMBER: _ClassVar[int]
AUDIT_LEVEL_ALL: AuditLevel
AUDIT_LEVEL_ERRORS: AuditLevel
AUDIT_LEVEL_UNSPECIFIED: AuditLevel
DESCRIPTOR: _descriptor.FileDescriptor
audit: _descriptor.FieldDescriptor

class AuditOptions(_message.Message):
    __slots__ = ["description", "level"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    description: str
    level: AuditLevel
    def __init__(self, level: _Optional[_Union[AuditLevel, str]] = ..., description: _Optional[str] = ...) -> None: ...

class AuditLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
