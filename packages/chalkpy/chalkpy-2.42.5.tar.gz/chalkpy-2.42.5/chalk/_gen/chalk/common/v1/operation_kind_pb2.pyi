from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
OPERATION_KIND_CRON: OperationKind
OPERATION_KIND_MIGRATION: OperationKind
OPERATION_KIND_MIGRATION_SAMPLER: OperationKind
OPERATION_KIND_OFFLINE_QUERY: OperationKind
OPERATION_KIND_ONLINE_QUERY: OperationKind
OPERATION_KIND_STREAMING: OperationKind
OPERATION_KIND_UNSPECIFIED: OperationKind
OPERATION_KIND_WINDOWED_STREAMING: OperationKind

class OperationKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
