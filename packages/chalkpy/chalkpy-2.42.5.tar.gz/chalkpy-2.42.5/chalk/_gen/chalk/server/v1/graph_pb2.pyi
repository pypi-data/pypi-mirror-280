from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from chalk._gen.chalk.graph.v1 import graph_pb2 as _graph_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureMetadata(_message.Message):
    __slots__ = ["description", "etl_offline_to_online", "fqn", "max_staleness", "name", "namespace", "owner", "tags"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETL_OFFLINE_TO_ONLINE_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    description: str
    etl_offline_to_online: bool
    fqn: str
    max_staleness: str
    name: str
    namespace: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        fqn: _Optional[str] = ...,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        max_staleness: _Optional[str] = ...,
        etl_offline_to_online: bool = ...,
    ) -> None: ...

class FeatureSQL(_message.Message):
    __slots__ = [
        "deployment_id",
        "description",
        "environment_id",
        "etl_offline_to_online",
        "fqn",
        "id",
        "internal_version",
        "is_singleton",
        "kind",
        "kind_enum",
        "max_staleness",
        "name",
        "namespace",
        "owner",
        "tags",
        "was_reset",
    ]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ETL_OFFLINE_TO_ONLINE_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_SINGLETON_FIELD_NUMBER: _ClassVar[int]
    KIND_ENUM_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    WAS_RESET_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    description: str
    environment_id: str
    etl_offline_to_online: bool
    fqn: str
    id: int
    internal_version: int
    is_singleton: bool
    kind: str
    kind_enum: str
    max_staleness: str
    name: str
    namespace: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    was_reset: bool
    def __init__(
        self,
        id: _Optional[int] = ...,
        environment_id: _Optional[str] = ...,
        deployment_id: _Optional[str] = ...,
        fqn: _Optional[str] = ...,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        max_staleness: _Optional[str] = ...,
        etl_offline_to_online: bool = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        kind_enum: _Optional[str] = ...,
        kind: _Optional[str] = ...,
        was_reset: bool = ...,
        internal_version: _Optional[int] = ...,
        is_singleton: bool = ...,
    ) -> None: ...

class GetFeatureSQLRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class GetFeatureSQLResponse(_message.Message):
    __slots__ = ["features"]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedCompositeFieldContainer[FeatureSQL]
    def __init__(self, features: _Optional[_Iterable[_Union[FeatureSQL, _Mapping]]] = ...) -> None: ...

class GetFeaturesMetadataRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetFeaturesMetadataResponse(_message.Message):
    __slots__ = ["deployment_id", "environment_id", "features"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    environment_id: str
    features: _containers.RepeatedCompositeFieldContainer[FeatureMetadata]
    def __init__(
        self,
        features: _Optional[_Iterable[_Union[FeatureMetadata, _Mapping]]] = ...,
        environment_id: _Optional[str] = ...,
        deployment_id: _Optional[str] = ...,
    ) -> None: ...

class GetGraphRequest(_message.Message):
    __slots__ = ["deployment_id"]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    def __init__(self, deployment_id: _Optional[str] = ...) -> None: ...

class GetGraphResponse(_message.Message):
    __slots__ = ["chalkpy_version", "graph", "tag"]
    CHALKPY_VERSION_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    chalkpy_version: str
    graph: _graph_pb2.Graph
    tag: str
    def __init__(
        self,
        graph: _Optional[_Union[_graph_pb2.Graph, _Mapping]] = ...,
        chalkpy_version: _Optional[str] = ...,
        tag: _Optional[str] = ...,
    ) -> None: ...

class UpdateGraphRequest(_message.Message):
    __slots__ = ["chalkpy_version", "deployment_id", "graph", "tag"]
    CHALKPY_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    chalkpy_version: str
    deployment_id: str
    graph: _graph_pb2.Graph
    tag: str
    def __init__(
        self,
        deployment_id: _Optional[str] = ...,
        graph: _Optional[_Union[_graph_pb2.Graph, _Mapping]] = ...,
        chalkpy_version: _Optional[str] = ...,
        tag: _Optional[str] = ...,
    ) -> None: ...

class UpdateGraphResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
