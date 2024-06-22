from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.auth.v1 import audit_pb2 as _audit_pb2
from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from chalk._gen.chalk.utils.v1 import sensitive_pb2 as _sensitive_pb2

DESCRIPTOR: _descriptor.FileDescriptor
PAGER_DUTY_EVENT_ACTION_ACKNOWLEDGE: PagerDutyEventAction
PAGER_DUTY_EVENT_ACTION_RESOLVE: PagerDutyEventAction
PAGER_DUTY_EVENT_ACTION_TRIGGER: PagerDutyEventAction
PAGER_DUTY_EVENT_ACTION_UNSPECIFIED: PagerDutyEventAction
PAGER_DUTY_SEVERITY_CRITICAL: PagerDutySeverity
PAGER_DUTY_SEVERITY_ERROR: PagerDutySeverity
PAGER_DUTY_SEVERITY_INFO: PagerDutySeverity
PAGER_DUTY_SEVERITY_UNSPECIFIED: PagerDutySeverity
PAGER_DUTY_SEVERITY_WARNING: PagerDutySeverity

class AddPagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["name", "token"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    token: str
    def __init__(self, name: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class AddPagerDutyIntegrationResponse(_message.Message):
    __slots__ = ["integration"]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PagerDutyIntegration
    def __init__(self, integration: _Optional[_Union[PagerDutyIntegration, _Mapping]] = ...) -> None: ...

class DeletePagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletePagerDutyIntegrationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllPagerDutyIntegrationsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllPagerDutyIntegrationsResponse(_message.Message):
    __slots__ = ["integrations"]
    INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
    integrations: _containers.RepeatedCompositeFieldContainer[PagerDutyIntegration]
    def __init__(self, integrations: _Optional[_Iterable[_Union[PagerDutyIntegration, _Mapping]]] = ...) -> None: ...

class GetPagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPagerDutyIntegrationResponse(_message.Message):
    __slots__ = ["integration"]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PagerDutyIntegration
    def __init__(self, integration: _Optional[_Union[PagerDutyIntegration, _Mapping]] = ...) -> None: ...

class PagerDutyEventV2(_message.Message):
    __slots__ = ["client", "client_url", "dedup_key", "event_action", "images", "links", "payload", "routing_key"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_URL_FIELD_NUMBER: _ClassVar[int]
    DEDUP_KEY_FIELD_NUMBER: _ClassVar[int]
    EVENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    client: str
    client_url: str
    dedup_key: str
    event_action: PagerDutyEventAction
    images: _containers.RepeatedCompositeFieldContainer[PagerDutyEventV2Image]
    links: _containers.RepeatedCompositeFieldContainer[PagerDutyEventV2Link]
    payload: PagerDutyEventV2Payload
    routing_key: str
    def __init__(
        self,
        payload: _Optional[_Union[PagerDutyEventV2Payload, _Mapping]] = ...,
        routing_key: _Optional[str] = ...,
        event_action: _Optional[_Union[PagerDutyEventAction, str]] = ...,
        dedup_key: _Optional[str] = ...,
        client: _Optional[str] = ...,
        client_url: _Optional[str] = ...,
        links: _Optional[_Iterable[_Union[PagerDutyEventV2Link, _Mapping]]] = ...,
        images: _Optional[_Iterable[_Union[PagerDutyEventV2Image, _Mapping]]] = ...,
    ) -> None: ...

class PagerDutyEventV2Image(_message.Message):
    __slots__ = ["alt", "href", "src"]
    ALT_FIELD_NUMBER: _ClassVar[int]
    HREF_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    alt: str
    href: str
    src: str
    def __init__(self, src: _Optional[str] = ..., href: _Optional[str] = ..., alt: _Optional[str] = ...) -> None: ...

class PagerDutyEventV2Link(_message.Message):
    __slots__ = ["href", "text"]
    HREF_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    href: str
    text: str
    def __init__(self, href: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class PagerDutyEventV2Payload(_message.Message):
    __slots__ = ["component", "group", "severity", "source", "summary", "timestamp"]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    component: str
    group: str
    severity: PagerDutySeverity
    source: str
    summary: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(
        self,
        summary: _Optional[str] = ...,
        timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        severity: _Optional[_Union[PagerDutySeverity, str]] = ...,
        source: _Optional[str] = ...,
        component: _Optional[str] = ...,
        group: _Optional[str] = ...,
        **kwargs,
    ) -> None: ...

class PagerDutyIntegration(_message.Message):
    __slots__ = ["default", "environment_id", "id", "name", "token"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    default: bool
    environment_id: str
    id: str
    name: str
    token: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        default: bool = ...,
        token: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
    ) -> None: ...

class SetDefaultPagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SetDefaultPagerDutyIntegrationResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TestPagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TestPagerDutyIntegrationResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UpdatePagerDutyIntegrationRequest(_message.Message):
    __slots__ = ["default", "id", "name", "token"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    default: bool
    id: str
    name: str
    token: str
    def __init__(
        self, id: _Optional[str] = ..., name: _Optional[str] = ..., default: bool = ..., token: _Optional[str] = ...
    ) -> None: ...

class UpdatePagerDutyIntegrationResponse(_message.Message):
    __slots__ = ["integration"]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: PagerDutyIntegration
    def __init__(self, integration: _Optional[_Union[PagerDutyIntegration, _Mapping]] = ...) -> None: ...

class PagerDutySeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PagerDutyEventAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
