from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor
HEALTH_CHECK_STATUS_FAILING: HealthCheckStatus
HEALTH_CHECK_STATUS_OK: HealthCheckStatus
HEALTH_CHECK_STATUS_UNSPECIFIED: HealthCheckStatus

class CheckHealthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CheckHealthResponse(_message.Message):
    __slots__ = ["checks"]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[HealthCheck]
    def __init__(self, checks: _Optional[_Iterable[_Union[HealthCheck, _Mapping]]] = ...) -> None: ...

class HealthCheck(_message.Message):
    __slots__ = ["message", "name", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    name: str
    status: HealthCheckStatus
    def __init__(
        self,
        name: _Optional[str] = ...,
        status: _Optional[_Union[HealthCheckStatus, str]] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...

class HealthCheckStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
