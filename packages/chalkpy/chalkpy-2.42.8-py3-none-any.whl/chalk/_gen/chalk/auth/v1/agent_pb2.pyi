from chalk._gen.chalk.auth.v1 import featurepermission_pb2 as _featurepermission_pb2
from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from google.protobuf.internal import containers as _containers
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

class Agent(_message.Message):
    __slots__ = ["engine_agent", "service_token_agent", "tenant_agent", "user_agent"]
    ENGINE_AGENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_AGENT_FIELD_NUMBER: _ClassVar[int]
    TENANT_AGENT_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    engine_agent: EngineAgent
    service_token_agent: ServiceTokenAgent
    tenant_agent: TenantAgent
    user_agent: UserAgent
    def __init__(
        self,
        user_agent: _Optional[_Union[UserAgent, _Mapping]] = ...,
        service_token_agent: _Optional[_Union[ServiceTokenAgent, _Mapping]] = ...,
        engine_agent: _Optional[_Union[EngineAgent, _Mapping]] = ...,
        tenant_agent: _Optional[_Union[TenantAgent, _Mapping]] = ...,
    ) -> None: ...

class CustomClaim(_message.Message):
    __slots__ = ["key", "values"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class EngineAgent(_message.Message):
    __slots__ = ["environment_id", "id", "impersonated", "project_id", "team_id"]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    environment_id: str
    id: str
    impersonated: bool
    project_id: str
    team_id: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        project_id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        impersonated: bool = ...,
    ) -> None: ...

class EnvironmentPermissions(_message.Message):
    __slots__ = ["feature_permissions", "permissions"]
    FEATURE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    feature_permissions: _featurepermission_pb2.FeaturePermissions
    permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    def __init__(
        self,
        permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
        feature_permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
    ) -> None: ...

class ServiceTokenAgent(_message.Message):
    __slots__ = [
        "client_id",
        "custom_claims",
        "customer_claims",
        "environment",
        "feature_permissions",
        "id",
        "permissions",
        "team_id",
    ]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    custom_claims: _containers.RepeatedScalarFieldContainer[str]
    customer_claims: _containers.RepeatedCompositeFieldContainer[CustomClaim]
    environment: str
    feature_permissions: _featurepermission_pb2.FeaturePermissions
    id: str
    permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    team_id: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        client_id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        environment: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
        custom_claims: _Optional[_Iterable[str]] = ...,
        customer_claims: _Optional[_Iterable[_Union[CustomClaim, _Mapping]]] = ...,
        feature_permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
    ) -> None: ...

class TenantAgent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserAgent(_message.Message):
    __slots__ = ["client_id", "impersonated", "permissions_by_environment", "team_id", "user_id"]
    class PermissionsByEnvironmentEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EnvironmentPermissions
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[_Union[EnvironmentPermissions, _Mapping]] = ...
        ) -> None: ...

    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    IMPERSONATED_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_BY_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    impersonated: bool
    permissions_by_environment: _containers.MessageMap[str, EnvironmentPermissions]
    team_id: str
    user_id: str
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        permissions_by_environment: _Optional[_Mapping[str, EnvironmentPermissions]] = ...,
        impersonated: bool = ...,
    ) -> None: ...
