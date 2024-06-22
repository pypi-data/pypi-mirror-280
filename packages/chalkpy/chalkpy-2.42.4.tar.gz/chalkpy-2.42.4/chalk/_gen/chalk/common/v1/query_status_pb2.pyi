from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
QUERY_STATUS_CANCELLED: QueryStatus
QUERY_STATUS_ERROR: QueryStatus
QUERY_STATUS_EXPIRED: QueryStatus
QUERY_STATUS_PENDING_SUBMISSION: QueryStatus
QUERY_STATUS_RUNNING: QueryStatus
QUERY_STATUS_SUBMITTED: QueryStatus
QUERY_STATUS_SUCCESSFUL: QueryStatus
QUERY_STATUS_SUCCESSFUL_WITH_NONFATAL_ERRORS: QueryStatus
QUERY_STATUS_UNSPECIFIED: QueryStatus

class QueryStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
