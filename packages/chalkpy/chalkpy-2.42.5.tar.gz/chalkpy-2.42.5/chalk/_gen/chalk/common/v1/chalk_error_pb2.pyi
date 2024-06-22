from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
ERROR_CODE_CANCELLED: ErrorCode
ERROR_CODE_CATEGORY_FIELD: ErrorCodeCategory
ERROR_CODE_CATEGORY_NETWORK_UNSPECIFIED: ErrorCodeCategory
ERROR_CODE_CATEGORY_REQUEST: ErrorCodeCategory
ERROR_CODE_DEADLINE_EXCEEDED: ErrorCode
ERROR_CODE_INTERNAL_SERVER_ERROR_UNSPECIFIED: ErrorCode
ERROR_CODE_INVALID_QUERY: ErrorCode
ERROR_CODE_PARSE_FAILED: ErrorCode
ERROR_CODE_RESOLVER_FAILED: ErrorCode
ERROR_CODE_RESOLVER_NOT_FOUND: ErrorCode
ERROR_CODE_RESOLVER_TIMED_OUT: ErrorCode
ERROR_CODE_UNAUTHENTICATED: ErrorCode
ERROR_CODE_UNAUTHORIZED: ErrorCode
ERROR_CODE_UPSTREAM_FAILED: ErrorCode
ERROR_CODE_VALIDATION_FAILED: ErrorCode

class ChalkError(_message.Message):
    __slots__ = [
        "category",
        "code",
        "display_primary_key",
        "display_primary_key_fqn",
        "exception",
        "feature",
        "message",
        "resolver",
    ]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_PRIMARY_KEY_FQN_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_FIELD_NUMBER: _ClassVar[int]
    category: ErrorCodeCategory
    code: ErrorCode
    display_primary_key: str
    display_primary_key_fqn: str
    exception: ChalkException
    feature: str
    message: str
    resolver: str
    def __init__(
        self,
        code: _Optional[_Union[ErrorCode, str]] = ...,
        category: _Optional[_Union[ErrorCodeCategory, str]] = ...,
        message: _Optional[str] = ...,
        display_primary_key: _Optional[str] = ...,
        display_primary_key_fqn: _Optional[str] = ...,
        exception: _Optional[_Union[ChalkException, _Mapping]] = ...,
        feature: _Optional[str] = ...,
        resolver: _Optional[str] = ...,
    ) -> None: ...

class ChalkException(_message.Message):
    __slots__ = ["internal_stacktrace", "kind", "message", "stacktrace"]
    INTERNAL_STACKTRACE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STACKTRACE_FIELD_NUMBER: _ClassVar[int]
    internal_stacktrace: str
    kind: str
    message: str
    stacktrace: str
    def __init__(
        self,
        kind: _Optional[str] = ...,
        message: _Optional[str] = ...,
        stacktrace: _Optional[str] = ...,
        internal_stacktrace: _Optional[str] = ...,
    ) -> None: ...

class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ErrorCodeCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
