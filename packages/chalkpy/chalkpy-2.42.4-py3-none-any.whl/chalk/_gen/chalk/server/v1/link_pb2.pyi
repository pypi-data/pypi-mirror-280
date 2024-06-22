from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.utils.v1 import sensitive_pb2 as _sensitive_pb2

DESCRIPTOR: _descriptor.FileDescriptor
LINK_SESSION_STATUS_FAILED: LinkSessionStatus
LINK_SESSION_STATUS_FORBIDDEN: LinkSessionStatus
LINK_SESSION_STATUS_NOT_FOUND: LinkSessionStatus
LINK_SESSION_STATUS_PENDING: LinkSessionStatus
LINK_SESSION_STATUS_SUCCESS: LinkSessionStatus
LINK_SESSION_STATUS_UNSPECIFIED: LinkSessionStatus

class CreateLinkSessionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateLinkSessionResponse(_message.Message):
    __slots__ = ["auth_link", "expires_at", "link_code"]
    AUTH_LINK_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LINK_CODE_FIELD_NUMBER: _ClassVar[int]
    auth_link: str
    expires_at: _timestamp_pb2.Timestamp
    link_code: str
    def __init__(
        self,
        link_code: _Optional[str] = ...,
        auth_link: _Optional[str] = ...,
        expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class GetLinkSessionRequest(_message.Message):
    __slots__ = ["link_code", "project_name"]
    LINK_CODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    link_code: str
    project_name: str
    def __init__(self, link_code: _Optional[str] = ..., project_name: _Optional[str] = ...) -> None: ...

class GetLinkSessionResponse(_message.Message):
    __slots__ = ["message", "status", "token"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: LinkSessionStatus
    token: LinkToken
    def __init__(
        self,
        status: _Optional[_Union[LinkSessionStatus, str]] = ...,
        message: _Optional[str] = ...,
        token: _Optional[_Union[LinkToken, _Mapping]] = ...,
    ) -> None: ...

class LinkToken(_message.Message):
    __slots__ = ["active_environment", "api_server", "client_id", "client_secret", "name", "valid_until"]
    ACTIVE_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    API_SERVER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    active_environment: str
    api_server: str
    client_id: str
    client_secret: str
    name: str
    valid_until: _timestamp_pb2.Timestamp
    def __init__(
        self,
        name: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        client_secret: _Optional[str] = ...,
        api_server: _Optional[str] = ...,
        active_environment: _Optional[str] = ...,
        valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class LinkSessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
