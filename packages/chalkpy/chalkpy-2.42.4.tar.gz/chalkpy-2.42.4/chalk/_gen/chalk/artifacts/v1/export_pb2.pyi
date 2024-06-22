from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.artifacts.v1 import cdc_pb2 as _cdc_pb2
from chalk._gen.chalk.artifacts.v1 import chart_pb2 as _chart_pb2
from chalk._gen.chalk.artifacts.v1 import cron_query_pb2 as _cron_query_pb2
from chalk._gen.chalk.graph.v1 import graph_pb2 as _graph_pb2
from chalk._gen.chalk.lsp.v1 import lsp_pb2 as _lsp_pb2

DESCRIPTOR: _descriptor.FileDescriptor
VALIDATION_LOG_SEVERITY_ERROR: ValidationLogSeverity
VALIDATION_LOG_SEVERITY_INFO: ValidationLogSeverity
VALIDATION_LOG_SEVERITY_UNSPECIFIED: ValidationLogSeverity
VALIDATION_LOG_SEVERITY_WARNING: ValidationLogSeverity

class ChalkpyInfo(_message.Message):
    __slots__ = ["python", "version"]
    PYTHON_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    python: str
    version: str
    def __init__(self, version: _Optional[str] = ..., python: _Optional[str] = ...) -> None: ...

class EnvironmentSettings(_message.Message):
    __slots__ = ["dockerfile", "id", "requirements", "requires_packages", "runtime"]
    DOCKERFILE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    dockerfile: str
    id: str
    requirements: str
    requires_packages: _containers.RepeatedScalarFieldContainer[str]
    runtime: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        runtime: _Optional[str] = ...,
        requirements: _Optional[str] = ...,
        dockerfile: _Optional[str] = ...,
        requires_packages: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class Export(_message.Message):
    __slots__ = ["cdc_sources", "chalkpy", "charts", "config", "crons", "failed", "graph", "logs", "lsp"]
    CDC_SOURCES_FIELD_NUMBER: _ClassVar[int]
    CHALKPY_FIELD_NUMBER: _ClassVar[int]
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CRONS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    GRAPH_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    LSP_FIELD_NUMBER: _ClassVar[int]
    cdc_sources: _containers.RepeatedCompositeFieldContainer[_cdc_pb2.CDCSource]
    chalkpy: ChalkpyInfo
    charts: _containers.RepeatedCompositeFieldContainer[_chart_pb2.Chart]
    config: ProjectSettings
    crons: _containers.RepeatedCompositeFieldContainer[_cron_query_pb2.CronQuery]
    failed: _containers.RepeatedCompositeFieldContainer[FailedImport]
    graph: _graph_pb2.Graph
    logs: _containers.RepeatedCompositeFieldContainer[ValidationLog]
    lsp: _lsp_pb2.LSP
    def __init__(
        self,
        graph: _Optional[_Union[_graph_pb2.Graph, _Mapping]] = ...,
        crons: _Optional[_Iterable[_Union[_cron_query_pb2.CronQuery, _Mapping]]] = ...,
        charts: _Optional[_Iterable[_Union[_chart_pb2.Chart, _Mapping]]] = ...,
        cdc_sources: _Optional[_Iterable[_Union[_cdc_pb2.CDCSource, _Mapping]]] = ...,
        config: _Optional[_Union[ProjectSettings, _Mapping]] = ...,
        chalkpy: _Optional[_Union[ChalkpyInfo, _Mapping]] = ...,
        failed: _Optional[_Iterable[_Union[FailedImport, _Mapping]]] = ...,
        logs: _Optional[_Iterable[_Union[ValidationLog, _Mapping]]] = ...,
        lsp: _Optional[_Union[_lsp_pb2.LSP, _Mapping]] = ...,
    ) -> None: ...

class FailedImport(_message.Message):
    __slots__ = ["file_name", "module", "traceback"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    TRACEBACK_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    module: str
    traceback: str
    def __init__(
        self, file_name: _Optional[str] = ..., module: _Optional[str] = ..., traceback: _Optional[str] = ...
    ) -> None: ...

class FeatureSettings(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.RepeatedCompositeFieldContainer[MetadataSettings]
    def __init__(self, metadata: _Optional[_Iterable[_Union[MetadataSettings, _Mapping]]] = ...) -> None: ...

class MetadataSettings(_message.Message):
    __slots__ = ["missing", "name"]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    missing: str
    name: str
    def __init__(self, name: _Optional[str] = ..., missing: _Optional[str] = ...) -> None: ...

class ProjectSettings(_message.Message):
    __slots__ = ["environments", "project", "validation"]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[EnvironmentSettings]
    project: str
    validation: ValidationSettings
    def __init__(
        self,
        project: _Optional[str] = ...,
        environments: _Optional[_Iterable[_Union[EnvironmentSettings, _Mapping]]] = ...,
        validation: _Optional[_Union[ValidationSettings, _Mapping]] = ...,
    ) -> None: ...

class ResolverSettings(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.RepeatedCompositeFieldContainer[MetadataSettings]
    def __init__(self, metadata: _Optional[_Iterable[_Union[MetadataSettings, _Mapping]]] = ...) -> None: ...

class ValidationLog(_message.Message):
    __slots__ = ["header", "severity", "subheader"]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SUBHEADER_FIELD_NUMBER: _ClassVar[int]
    header: str
    severity: ValidationLogSeverity
    subheader: str
    def __init__(
        self,
        header: _Optional[str] = ...,
        subheader: _Optional[str] = ...,
        severity: _Optional[_Union[ValidationLogSeverity, str]] = ...,
    ) -> None: ...

class ValidationSettings(_message.Message):
    __slots__ = ["feature", "resolver"]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_FIELD_NUMBER: _ClassVar[int]
    feature: FeatureSettings
    resolver: ResolverSettings
    def __init__(
        self,
        feature: _Optional[_Union[FeatureSettings, _Mapping]] = ...,
        resolver: _Optional[_Union[ResolverSettings, _Mapping]] = ...,
    ) -> None: ...

class ValidationLogSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
