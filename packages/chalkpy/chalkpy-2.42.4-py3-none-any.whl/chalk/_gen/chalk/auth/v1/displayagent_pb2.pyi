from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.auth.v1 import featurepermission_pb2 as _featurepermission_pb2
from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayAgent(_message.Message):
    __slots__ = ["engine_agent", "service_token_agent", "tenant_agent", "user_agent"]
    ENGINE_AGENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_AGENT_FIELD_NUMBER: _ClassVar[int]
    TENANT_AGENT_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    engine_agent: DisplayEngineAgent
    service_token_agent: DisplayServiceTokenAgent
    tenant_agent: DisplayTenantAgent
    user_agent: DisplayUserAgent
    def __init__(
        self,
        user_agent: _Optional[_Union[DisplayUserAgent, _Mapping]] = ...,
        service_token_agent: _Optional[_Union[DisplayServiceTokenAgent, _Mapping]] = ...,
        engine_agent: _Optional[_Union[DisplayEngineAgent, _Mapping]] = ...,
        tenant_agent: _Optional[_Union[DisplayTenantAgent, _Mapping]] = ...,
    ) -> None: ...

class DisplayCustomClaim(_message.Message):
    __slots__ = ["key", "values"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class DisplayEngineAgent(_message.Message):
    __slots__ = [
        "environment_id",
        "environment_name",
        "id",
        "impersonated",
        "project_id",
        "project_name",
        "team_id",
        "team_name",
    ]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    environment_name: str
    id: str
    impersonated: bool
    project_id: str
    project_name: str
    team_id: str
    team_name: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        project_id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        impersonated: bool = ...,
        team_name: _Optional[str] = ...,
        project_name: _Optional[str] = ...,
        environment_name: _Optional[str] = ...,
    ) -> None: ...

class DisplayEnvironmentPermissions(_message.Message):
    __slots__ = ["environment_id", "environment_name", "permissions", "project_id", "project_name"]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    environment_name: str
    permissions: _containers.RepeatedCompositeFieldContainer[DisplayPermission]
    project_id: str
    project_name: str
    def __init__(
        self,
        environment_id: _Optional[str] = ...,
        environment_name: _Optional[str] = ...,
        project_id: _Optional[str] = ...,
        project_name: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[DisplayPermission, _Mapping]]] = ...,
    ) -> None: ...

class DisplayPermission(_message.Message):
    __slots__ = ["name", "permission"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    permission: _permissions_pb2.Permission
    def __init__(
        self, name: _Optional[str] = ..., permission: _Optional[_Union[_permissions_pb2.Permission, str]] = ...
    ) -> None: ...

class DisplayServiceTokenAgent(_message.Message):
    __slots__ = [
        "client_id",
        "created_at",
        "customer_claims",
        "environment_id",
        "environment_name",
        "feature_permissions",
        "id",
        "name",
        "permissions",
        "project_id",
        "project_name",
        "team_id",
        "team_name",
    ]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    created_at: _timestamp_pb2.Timestamp
    customer_claims: _containers.RepeatedCompositeFieldContainer[DisplayCustomClaim]
    environment_id: str
    environment_name: str
    feature_permissions: _featurepermission_pb2.FeaturePermissions
    id: str
    name: str
    permissions: _containers.RepeatedCompositeFieldContainer[DisplayPermission]
    project_id: str
    project_name: str
    team_id: str
    team_name: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        project_id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[DisplayPermission, _Mapping]]] = ...,
        name: _Optional[str] = ...,
        team_name: _Optional[str] = ...,
        project_name: _Optional[str] = ...,
        environment_name: _Optional[str] = ...,
        customer_claims: _Optional[_Iterable[_Union[DisplayCustomClaim, _Mapping]]] = ...,
        feature_permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
        created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class DisplayTenantAgent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DisplayUserAgent(_message.Message):
    __slots__ = [
        "client_id",
        "email",
        "impersonated",
        "name",
        "permissions_by_environment",
        "team_id",
        "team_name",
        "user_id",
    ]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_BY_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    email: str
    impersonated: bool
    name: str
    permissions_by_environment: _containers.RepeatedCompositeFieldContainer[DisplayEnvironmentPermissions]
    team_id: str
    team_name: str
    user_id: str
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        permissions_by_environment: _Optional[_Iterable[_Union[DisplayEnvironmentPermissions, _Mapping]]] = ...,
        impersonated: bool = ...,
        name: _Optional[str] = ...,
        email: _Optional[str] = ...,
        team_name: _Optional[str] = ...,
    ) -> None: ...
