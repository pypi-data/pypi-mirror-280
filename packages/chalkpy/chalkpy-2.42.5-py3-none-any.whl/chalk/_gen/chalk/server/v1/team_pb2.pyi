from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.auth.v1 import agent_pb2 as _agent_pb2
from chalk._gen.chalk.auth.v1 import audit_pb2 as _audit_pb2
from chalk._gen.chalk.auth.v1 import displayagent_pb2 as _displayagent_pb2
from chalk._gen.chalk.auth.v1 import featurepermission_pb2 as _featurepermission_pb2
from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from chalk._gen.chalk.server.v1 import environment_pb2 as _environment_pb2
from chalk._gen.chalk.utils.v1 import sensitive_pb2 as _sensitive_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ["is_default", "name", "project_id"]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    is_default: bool
    name: str
    project_id: str
    def __init__(
        self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., is_default: bool = ...
    ) -> None: ...

class CreateEnvironmentResponse(_message.Message):
    __slots__ = ["environment"]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: _environment_pb2.Environment
    def __init__(self, environment: _Optional[_Union[_environment_pb2.Environment, _Mapping]] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ...) -> None: ...

class CreateServiceTokenRequest(_message.Message):
    __slots__ = ["custom_claims", "customer_claims", "feature_tag_to_permission", "name", "permissions"]
    class FeatureTagToPermissionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _featurepermission_pb2.FeaturePermission
        def __init__(
            self,
            key: _Optional[str] = ...,
            value: _Optional[_Union[_featurepermission_pb2.FeaturePermission, str]] = ...,
        ) -> None: ...

    CUSTOMER_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TAG_TO_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    custom_claims: _containers.RepeatedScalarFieldContainer[str]
    customer_claims: _containers.RepeatedCompositeFieldContainer[_agent_pb2.CustomClaim]
    feature_tag_to_permission: _containers.ScalarMap[str, _featurepermission_pb2.FeaturePermission]
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    def __init__(
        self,
        name: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
        custom_claims: _Optional[_Iterable[str]] = ...,
        customer_claims: _Optional[_Iterable[_Union[_agent_pb2.CustomClaim, _Mapping]]] = ...,
        feature_tag_to_permission: _Optional[_Mapping[str, _featurepermission_pb2.FeaturePermission]] = ...,
    ) -> None: ...

class CreateServiceTokenResponse(_message.Message):
    __slots__ = ["agent", "client_secret"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    agent: _agent_pb2.ServiceTokenAgent
    client_secret: str
    def __init__(
        self,
        agent: _Optional[_Union[_agent_pb2.ServiceTokenAgent, _Mapping]] = ...,
        client_secret: _Optional[str] = ...,
    ) -> None: ...

class CreateTeamRequest(_message.Message):
    __slots__ = ["logo", "name", "slug"]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    logo: str
    name: str
    slug: str
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ..., logo: _Optional[str] = ...) -> None: ...

class CreateTeamResponse(_message.Message):
    __slots__ = ["team"]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class DeleteServiceTokenRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteServiceTokenResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAgentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAgentResponse(_message.Message):
    __slots__ = ["agent"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: _agent_pb2.Agent
    def __init__(self, agent: _Optional[_Union[_agent_pb2.Agent, _Mapping]] = ...) -> None: ...

class GetAvailablePermissionsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAvailablePermissionsResponse(_message.Message):
    __slots__ = ["available_service_token_permissions", "permissions", "roles"]
    AVAILABLE_SERVICE_TOKEN_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    available_service_token_permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    permissions: _containers.RepeatedCompositeFieldContainer[PermissionDescription]
    roles: _containers.RepeatedCompositeFieldContainer[RoleDescription]
    def __init__(
        self,
        permissions: _Optional[_Iterable[_Union[PermissionDescription, _Mapping]]] = ...,
        roles: _Optional[_Iterable[_Union[RoleDescription, _Mapping]]] = ...,
        available_service_token_permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
    ) -> None: ...

class GetDisplayAgentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDisplayAgentResponse(_message.Message):
    __slots__ = ["agent"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: _displayagent_pb2.DisplayAgent
    def __init__(self, agent: _Optional[_Union[_displayagent_pb2.DisplayAgent, _Mapping]] = ...) -> None: ...

class GetEnvRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetEnvResponse(_message.Message):
    __slots__ = ["environment"]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: _environment_pb2.Environment
    def __init__(self, environment: _Optional[_Union[_environment_pb2.Environment, _Mapping]] = ...) -> None: ...

class GetEnvironmentsRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class GetEnvironmentsResponse(_message.Message):
    __slots__ = ["environments"]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[_environment_pb2.Environment]
    def __init__(
        self, environments: _Optional[_Iterable[_Union[_environment_pb2.Environment, _Mapping]]] = ...
    ) -> None: ...

class GetTeamRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTeamResponse(_message.Message):
    __slots__ = ["team"]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: Team
    def __init__(self, team: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...

class ListServiceTokensRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListServiceTokensResponse(_message.Message):
    __slots__ = ["agents"]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[_displayagent_pb2.DisplayServiceTokenAgent]
    def __init__(
        self, agents: _Optional[_Iterable[_Union[_displayagent_pb2.DisplayServiceTokenAgent, _Mapping]]] = ...
    ) -> None: ...

class PermissionDescription(_message.Message):
    __slots__ = ["description", "group_description", "id", "name", "namespace", "slug"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    description: str
    group_description: str
    id: _permissions_pb2.Permission
    name: str
    namespace: str
    slug: str
    def __init__(
        self,
        id: _Optional[_Union[_permissions_pb2.Permission, str]] = ...,
        slug: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        group_description: _Optional[str] = ...,
    ) -> None: ...

class Project(_message.Message):
    __slots__ = ["environments", "id", "name", "team_id"]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[_environment_pb2.Environment]
    id: str
    name: str
    team_id: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        environments: _Optional[_Iterable[_Union[_environment_pb2.Environment, _Mapping]]] = ...,
    ) -> None: ...

class RoleDescription(_message.Message):
    __slots__ = ["description", "feature_permissions", "id", "is_default", "name", "permissions"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEATURE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    description: str
    feature_permissions: _featurepermission_pb2.FeaturePermissions
    id: str
    is_default: bool
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
        feature_permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
        is_default: bool = ...,
    ) -> None: ...

class Team(_message.Message):
    __slots__ = ["id", "logo", "name", "projects", "slug"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    id: str
    logo: str
    name: str
    projects: _containers.RepeatedCompositeFieldContainer[Project]
    slug: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        slug: _Optional[str] = ...,
        logo: _Optional[str] = ...,
        projects: _Optional[_Iterable[_Union[Project, _Mapping]]] = ...,
    ) -> None: ...

class UpdateServiceTokenRequest(_message.Message):
    __slots__ = ["client_id", "customer_claims", "feature_tag_to_permission", "name", "permissions"]
    class FeatureTagToPermissionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _featurepermission_pb2.FeaturePermission
        def __init__(
            self,
            key: _Optional[str] = ...,
            value: _Optional[_Union[_featurepermission_pb2.FeaturePermission, str]] = ...,
        ) -> None: ...

    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TAG_TO_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    customer_claims: _containers.RepeatedCompositeFieldContainer[_agent_pb2.CustomClaim]
    feature_tag_to_permission: _containers.ScalarMap[str, _featurepermission_pb2.FeaturePermission]
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[_permissions_pb2.Permission]
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        permissions: _Optional[_Iterable[_Union[_permissions_pb2.Permission, str]]] = ...,
        customer_claims: _Optional[_Iterable[_Union[_agent_pb2.CustomClaim, _Mapping]]] = ...,
        feature_tag_to_permission: _Optional[_Mapping[str, _featurepermission_pb2.FeaturePermission]] = ...,
    ) -> None: ...

class UpdateServiceTokenResponse(_message.Message):
    __slots__ = ["agent"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    agent: _displayagent_pb2.DisplayServiceTokenAgent
    def __init__(
        self, agent: _Optional[_Union[_displayagent_pb2.DisplayServiceTokenAgent, _Mapping]] = ...
    ) -> None: ...

class UpsertFeaturePermissionsRequest(_message.Message):
    __slots__ = ["permissions", "role"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    permissions: _featurepermission_pb2.FeaturePermissions
    role: str
    def __init__(
        self,
        role: _Optional[str] = ...,
        permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
    ) -> None: ...

class UpsertFeaturePermissionsResponse(_message.Message):
    __slots__ = ["permissions", "role"]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    permissions: _featurepermission_pb2.FeaturePermissions
    role: str
    def __init__(
        self,
        role: _Optional[str] = ...,
        permissions: _Optional[_Union[_featurepermission_pb2.FeaturePermissions, _Mapping]] = ...,
    ) -> None: ...
