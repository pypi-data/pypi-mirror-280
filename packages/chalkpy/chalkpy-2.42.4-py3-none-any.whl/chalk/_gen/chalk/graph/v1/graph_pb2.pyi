from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.arrow.v1 import arrow_pb2 as _arrow_pb2
from chalk._gen.chalk.expression.v1 import expression_pb2 as _expression_pb2
from chalk._gen.chalk.graph.v1 import sources_pb2 as _sources_pb2

DESCRIPTOR: _descriptor.FileDescriptor
RESOLVER_KIND_OFFLINE: ResolverKind
RESOLVER_KIND_ONLINE: ResolverKind
RESOLVER_KIND_UNSPECIFIED: ResolverKind
WINDOW_MODE_CDC: WindowMode
WINDOW_MODE_CONTINUOUS: WindowMode
WINDOW_MODE_TUMBLING: WindowMode
WINDOW_MODE_UNSPECIFIED: WindowMode

class CronFilterWithFeatureArgs(_message.Message):
    __slots__ = ["args", "filter"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedCompositeFieldContainer[FeatureReference]
    filter: FunctionReference
    def __init__(
        self,
        filter: _Optional[_Union[FunctionReference, _Mapping]] = ...,
        args: _Optional[_Iterable[_Union[FeatureReference, _Mapping]]] = ...,
    ) -> None: ...

class DataFrameType(_message.Message):
    __slots__ = ["filter", "limit", "optional_columns", "required_columns", "root_namespace"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ROOT_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    filter: _expression_pb2.LogicalExprNode
    limit: int
    optional_columns: _containers.RepeatedCompositeFieldContainer[FeatureReference]
    required_columns: _containers.RepeatedCompositeFieldContainer[FeatureReference]
    root_namespace: str
    def __init__(
        self,
        root_namespace: _Optional[str] = ...,
        required_columns: _Optional[_Iterable[_Union[FeatureReference, _Mapping]]] = ...,
        optional_columns: _Optional[_Iterable[_Union[FeatureReference, _Mapping]]] = ...,
        filter: _Optional[_Union[_expression_pb2.LogicalExprNode, _Mapping]] = ...,
        limit: _Optional[int] = ...,
    ) -> None: ...

class FeatureInput(_message.Message):
    __slots__ = ["default_value", "feature"]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    default_value: _arrow_pb2.ScalarValue
    feature: FeatureReference
    def __init__(
        self,
        feature: _Optional[_Union[FeatureReference, _Mapping]] = ...,
        default_value: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...,
    ) -> None: ...

class FeatureReference(_message.Message):
    __slots__ = ["df", "name", "namespace", "path"]
    DF_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    df: DataFrameType
    name: str
    namespace: str
    path: _containers.RepeatedCompositeFieldContainer[FeatureReference]
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        path: _Optional[_Iterable[_Union[FeatureReference, _Mapping]]] = ...,
        df: _Optional[_Union[DataFrameType, _Mapping]] = ...,
    ) -> None: ...

class FeatureSet(_message.Message):
    __slots__ = [
        "class_path",
        "doc",
        "etl_offline_to_online",
        "features",
        "is_singleton",
        "max_staleness_duration",
        "name",
        "owner",
        "tags",
    ]
    CLASS_PATH_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    ETL_OFFLINE_TO_ONLINE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    IS_SINGLETON_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    class_path: str
    doc: str
    etl_offline_to_online: bool
    features: _containers.RepeatedCompositeFieldContainer[FeatureType]
    is_singleton: bool
    max_staleness_duration: _duration_pb2.Duration
    name: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        features: _Optional[_Iterable[_Union[FeatureType, _Mapping]]] = ...,
        max_staleness_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        is_singleton: bool = ...,
        tags: _Optional[_Iterable[str]] = ...,
        owner: _Optional[str] = ...,
        doc: _Optional[str] = ...,
        etl_offline_to_online: bool = ...,
        class_path: _Optional[str] = ...,
    ) -> None: ...

class FeatureTimeFeatureType(_message.Message):
    __slots__ = ["attribute_name", "description", "is_autogenerated", "name", "namespace", "owner", "tags"]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    attribute_name: str
    description: str
    is_autogenerated: bool
    name: str
    namespace: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        is_autogenerated: bool = ...,
        tags: _Optional[_Iterable[str]] = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        attribute_name: _Optional[str] = ...,
    ) -> None: ...

class FeatureType(_message.Message):
    __slots__ = ["feature_time", "has_many", "has_one", "scalar", "windowed"]
    FEATURE_TIME_FIELD_NUMBER: _ClassVar[int]
    HAS_MANY_FIELD_NUMBER: _ClassVar[int]
    HAS_ONE_FIELD_NUMBER: _ClassVar[int]
    SCALAR_FIELD_NUMBER: _ClassVar[int]
    WINDOWED_FIELD_NUMBER: _ClassVar[int]
    feature_time: FeatureTimeFeatureType
    has_many: HasManyFeatureType
    has_one: HasOneFeatureType
    scalar: ScalarFeatureType
    windowed: WindowedFeatureType
    def __init__(
        self,
        scalar: _Optional[_Union[ScalarFeatureType, _Mapping]] = ...,
        has_one: _Optional[_Union[HasOneFeatureType, _Mapping]] = ...,
        has_many: _Optional[_Union[HasManyFeatureType, _Mapping]] = ...,
        feature_time: _Optional[_Union[FeatureTimeFeatureType, _Mapping]] = ...,
        windowed: _Optional[_Union[WindowedFeatureType, _Mapping]] = ...,
    ) -> None: ...

class FeatureValidation(_message.Message):
    __slots__ = ["max", "max_length", "min", "min_length", "strict"]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    STRICT_FIELD_NUMBER: _ClassVar[int]
    max: float
    max_length: int
    min: float
    min_length: int
    strict: bool
    def __init__(
        self,
        min: _Optional[float] = ...,
        max: _Optional[float] = ...,
        min_length: _Optional[int] = ...,
        max_length: _Optional[int] = ...,
        strict: bool = ...,
    ) -> None: ...

class FunctionReference(_message.Message):
    __slots__ = ["file_name", "function_definition", "module", "name", "source_line"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LINE_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    function_definition: str
    module: str
    name: str
    source_line: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        module: _Optional[str] = ...,
        file_name: _Optional[str] = ...,
        function_definition: _Optional[str] = ...,
        source_line: _Optional[int] = ...,
    ) -> None: ...

class Graph(_message.Message):
    __slots__ = [
        "database_sources",
        "feature_sets",
        "resolvers",
        "sink_resolvers",
        "stream_resolvers",
        "stream_sources",
    ]
    DATABASE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    FEATURE_SETS_FIELD_NUMBER: _ClassVar[int]
    RESOLVERS_FIELD_NUMBER: _ClassVar[int]
    SINK_RESOLVERS_FIELD_NUMBER: _ClassVar[int]
    STREAM_RESOLVERS_FIELD_NUMBER: _ClassVar[int]
    STREAM_SOURCES_FIELD_NUMBER: _ClassVar[int]
    database_sources: _containers.RepeatedCompositeFieldContainer[_sources_pb2.DatabaseSource]
    feature_sets: _containers.RepeatedCompositeFieldContainer[FeatureSet]
    resolvers: _containers.RepeatedCompositeFieldContainer[Resolver]
    sink_resolvers: _containers.RepeatedCompositeFieldContainer[SinkResolver]
    stream_resolvers: _containers.RepeatedCompositeFieldContainer[StreamResolver]
    stream_sources: _containers.RepeatedCompositeFieldContainer[_sources_pb2.StreamSource]
    def __init__(
        self,
        feature_sets: _Optional[_Iterable[_Union[FeatureSet, _Mapping]]] = ...,
        resolvers: _Optional[_Iterable[_Union[Resolver, _Mapping]]] = ...,
        stream_resolvers: _Optional[_Iterable[_Union[StreamResolver, _Mapping]]] = ...,
        sink_resolvers: _Optional[_Iterable[_Union[SinkResolver, _Mapping]]] = ...,
        database_sources: _Optional[_Iterable[_Union[_sources_pb2.DatabaseSource, _Mapping]]] = ...,
        stream_sources: _Optional[_Iterable[_Union[_sources_pb2.StreamSource, _Mapping]]] = ...,
    ) -> None: ...

class HasManyFeatureType(_message.Message):
    __slots__ = [
        "attribute_name",
        "description",
        "foreign_namespace",
        "is_autogenerated",
        "join",
        "max_staleness_duration",
        "name",
        "namespace",
        "owner",
        "tags",
    ]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    attribute_name: str
    description: str
    foreign_namespace: str
    is_autogenerated: bool
    join: _expression_pb2.LogicalExprNode
    max_staleness_duration: _duration_pb2.Duration
    name: str
    namespace: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        foreign_namespace: _Optional[str] = ...,
        join: _Optional[_Union[_expression_pb2.LogicalExprNode, _Mapping]] = ...,
        is_autogenerated: bool = ...,
        max_staleness_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        attribute_name: _Optional[str] = ...,
    ) -> None: ...

class HasOneFeatureType(_message.Message):
    __slots__ = [
        "attribute_name",
        "description",
        "foreign_namespace",
        "is_autogenerated",
        "is_nullable",
        "join",
        "name",
        "namespace",
        "owner",
        "tags",
    ]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    IS_NULLABLE_FIELD_NUMBER: _ClassVar[int]
    JOIN_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    attribute_name: str
    description: str
    foreign_namespace: str
    is_autogenerated: bool
    is_nullable: bool
    join: _expression_pb2.LogicalExprNode
    name: str
    namespace: str
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        foreign_namespace: _Optional[str] = ...,
        join: _Optional[_Union[_expression_pb2.LogicalExprNode, _Mapping]] = ...,
        is_nullable: bool = ...,
        is_autogenerated: bool = ...,
        tags: _Optional[_Iterable[str]] = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        attribute_name: _Optional[str] = ...,
    ) -> None: ...

class ParseInfo(_message.Message):
    __slots__ = [
        "is_parse_function_output_optional",
        "parse_function",
        "parse_function_input_type",
        "parse_function_output_type",
    ]
    IS_PARSE_FUNCTION_OUTPUT_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    PARSE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    PARSE_FUNCTION_INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARSE_FUNCTION_OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_parse_function_output_optional: bool
    parse_function: FunctionReference
    parse_function_input_type: _arrow_pb2.ArrowType
    parse_function_output_type: _arrow_pb2.ArrowType
    def __init__(
        self,
        parse_function: _Optional[_Union[FunctionReference, _Mapping]] = ...,
        parse_function_input_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
        parse_function_output_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
        is_parse_function_output_optional: bool = ...,
    ) -> None: ...

class Resolver(_message.Message):
    __slots__ = [
        "cron_filter",
        "data_sources",
        "doc",
        "environments",
        "fqn",
        "function",
        "inputs",
        "is_generator",
        "kind",
        "machine_type",
        "outputs",
        "owner",
        "schedule",
        "tags",
        "timeout_duration",
        "when",
    ]
    CRON_FILTER_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    IS_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    WHEN_FIELD_NUMBER: _ClassVar[int]
    cron_filter: CronFilterWithFeatureArgs
    data_sources: _containers.RepeatedCompositeFieldContainer[_sources_pb2.DatabaseSourceReference]
    doc: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    fqn: str
    function: FunctionReference
    inputs: _containers.RepeatedCompositeFieldContainer[ResolverInput]
    is_generator: bool
    kind: ResolverKind
    machine_type: str
    outputs: _containers.RepeatedCompositeFieldContainer[ResolverOutput]
    owner: str
    schedule: Schedule
    tags: _containers.RepeatedScalarFieldContainer[str]
    timeout_duration: _duration_pb2.Duration
    when: _expression_pb2.LogicalExprNode
    def __init__(
        self,
        fqn: _Optional[str] = ...,
        kind: _Optional[_Union[ResolverKind, str]] = ...,
        inputs: _Optional[_Iterable[_Union[ResolverInput, _Mapping]]] = ...,
        outputs: _Optional[_Iterable[_Union[ResolverOutput, _Mapping]]] = ...,
        is_generator: bool = ...,
        data_sources: _Optional[_Iterable[_Union[_sources_pb2.DatabaseSourceReference, _Mapping]]] = ...,
        machine_type: _Optional[str] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        owner: _Optional[str] = ...,
        doc: _Optional[str] = ...,
        environments: _Optional[_Iterable[str]] = ...,
        timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        schedule: _Optional[_Union[Schedule, _Mapping]] = ...,
        when: _Optional[_Union[_expression_pb2.LogicalExprNode, _Mapping]] = ...,
        cron_filter: _Optional[_Union[CronFilterWithFeatureArgs, _Mapping]] = ...,
        function: _Optional[_Union[FunctionReference, _Mapping]] = ...,
    ) -> None: ...

class ResolverInput(_message.Message):
    __slots__ = ["df", "feature", "state"]
    DF_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    df: DataFrameType
    feature: FeatureInput
    state: ResolverState
    def __init__(
        self,
        feature: _Optional[_Union[FeatureInput, _Mapping]] = ...,
        df: _Optional[_Union[DataFrameType, _Mapping]] = ...,
        state: _Optional[_Union[ResolverState, _Mapping]] = ...,
    ) -> None: ...

class ResolverOutput(_message.Message):
    __slots__ = ["df", "feature"]
    DF_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    df: DataFrameType
    feature: FeatureReference
    def __init__(
        self,
        feature: _Optional[_Union[FeatureReference, _Mapping]] = ...,
        df: _Optional[_Union[DataFrameType, _Mapping]] = ...,
    ) -> None: ...

class ResolverState(_message.Message):
    __slots__ = ["arrow_type", "initial"]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    initial: _arrow_pb2.ScalarValue
    def __init__(
        self,
        initial: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...,
        arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
    ) -> None: ...

class ScalarFeatureType(_message.Message):
    __slots__ = [
        "arrow_type",
        "attribute_name",
        "default_value",
        "description",
        "etl_offline_to_online",
        "expression",
        "internal_version",
        "is_autogenerated",
        "is_distance_pseudofeature",
        "is_nullable",
        "is_primary",
        "last_for",
        "max_staleness_duration",
        "name",
        "namespace",
        "no_display",
        "offline_ttl_duration",
        "owner",
        "tags",
        "validations",
        "version",
        "window_info",
    ]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETL_OFFLINE_TO_ONLINE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    IS_DISTANCE_PSEUDOFEATURE_FIELD_NUMBER: _ClassVar[int]
    IS_NULLABLE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    LAST_FOR_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_TTL_DURATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_INFO_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    attribute_name: str
    default_value: _arrow_pb2.ScalarValue
    description: str
    etl_offline_to_online: bool
    expression: _expression_pb2.LogicalExprNode
    internal_version: int
    is_autogenerated: bool
    is_distance_pseudofeature: bool
    is_nullable: bool
    is_primary: bool
    last_for: FeatureReference
    max_staleness_duration: _duration_pb2.Duration
    name: str
    namespace: str
    no_display: bool
    offline_ttl_duration: _duration_pb2.Duration
    owner: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    validations: _containers.RepeatedCompositeFieldContainer[FeatureValidation]
    version: VersionInfo
    window_info: WindowInfo
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        is_autogenerated: bool = ...,
        no_display: bool = ...,
        is_primary: bool = ...,
        is_nullable: bool = ...,
        internal_version: _Optional[int] = ...,
        max_staleness_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        offline_ttl_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
        version: _Optional[_Union[VersionInfo, _Mapping]] = ...,
        window_info: _Optional[_Union[WindowInfo, _Mapping]] = ...,
        default_value: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        description: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        expression: _Optional[_Union[_expression_pb2.LogicalExprNode, _Mapping]] = ...,
        validations: _Optional[_Iterable[_Union[FeatureValidation, _Mapping]]] = ...,
        last_for: _Optional[_Union[FeatureReference, _Mapping]] = ...,
        etl_offline_to_online: bool = ...,
        is_distance_pseudofeature: bool = ...,
        attribute_name: _Optional[str] = ...,
    ) -> None: ...

class Schedule(_message.Message):
    __slots__ = ["crontab", "duration", "filter", "sample"]
    CRONTAB_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    crontab: str
    duration: _duration_pb2.Duration
    filter: FunctionReference
    sample: FunctionReference
    def __init__(
        self,
        crontab: _Optional[str] = ...,
        duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        filter: _Optional[_Union[FunctionReference, _Mapping]] = ...,
        sample: _Optional[_Union[FunctionReference, _Mapping]] = ...,
    ) -> None: ...

class SinkResolver(_message.Message):
    __slots__ = [
        "buffer_size",
        "database_source",
        "debounce_duration",
        "doc",
        "environments",
        "fqn",
        "function",
        "inputs",
        "machine_type",
        "max_delay_duration",
        "owner",
        "stream_source",
        "timeout_duration",
        "upsert",
    ]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DEBOUNCE_DURATION_FIELD_NUMBER: _ClassVar[int]
    DOC_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_DELAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    STREAM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    UPSERT_FIELD_NUMBER: _ClassVar[int]
    buffer_size: int
    database_source: _sources_pb2.DatabaseSourceReference
    debounce_duration: _duration_pb2.Duration
    doc: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    fqn: str
    function: FunctionReference
    inputs: _containers.RepeatedCompositeFieldContainer[ResolverInput]
    machine_type: str
    max_delay_duration: _duration_pb2.Duration
    owner: str
    stream_source: _sources_pb2.StreamSourceReference
    timeout_duration: _duration_pb2.Duration
    upsert: bool
    def __init__(
        self,
        fqn: _Optional[str] = ...,
        inputs: _Optional[_Iterable[_Union[ResolverInput, _Mapping]]] = ...,
        buffer_size: _Optional[int] = ...,
        debounce_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        max_delay_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        upsert: bool = ...,
        stream_source: _Optional[_Union[_sources_pb2.StreamSourceReference, _Mapping]] = ...,
        database_source: _Optional[_Union[_sources_pb2.DatabaseSourceReference, _Mapping]] = ...,
        machine_type: _Optional[str] = ...,
        doc: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        environments: _Optional[_Iterable[str]] = ...,
        timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        function: _Optional[_Union[FunctionReference, _Mapping]] = ...,
    ) -> None: ...

class StreamKey(_message.Message):
    __slots__ = ["feature", "key"]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    feature: FeatureReference
    key: str
    def __init__(
        self, key: _Optional[str] = ..., feature: _Optional[_Union[FeatureReference, _Mapping]] = ...
    ) -> None: ...

class StreamResolver(_message.Message):
    __slots__ = [
        "doc",
        "environments",
        "explicit_schema",
        "fqn",
        "function",
        "keys",
        "machine_type",
        "mode",
        "outputs",
        "owner",
        "params",
        "parse_info",
        "source",
        "timeout_duration",
        "timestamp_attribute_name",
    ]
    DOC_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FQN_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARSE_INFO_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    doc: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    explicit_schema: _arrow_pb2.ArrowType
    fqn: str
    function: FunctionReference
    keys: _containers.RepeatedCompositeFieldContainer[StreamKey]
    machine_type: str
    mode: WindowMode
    outputs: _containers.RepeatedCompositeFieldContainer[ResolverOutput]
    owner: str
    params: _containers.RepeatedCompositeFieldContainer[StreamResolverParam]
    parse_info: ParseInfo
    source: _sources_pb2.StreamSourceReference
    timeout_duration: _duration_pb2.Duration
    timestamp_attribute_name: str
    def __init__(
        self,
        fqn: _Optional[str] = ...,
        params: _Optional[_Iterable[_Union[StreamResolverParam, _Mapping]]] = ...,
        outputs: _Optional[_Iterable[_Union[ResolverOutput, _Mapping]]] = ...,
        explicit_schema: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
        keys: _Optional[_Iterable[_Union[StreamKey, _Mapping]]] = ...,
        source: _Optional[_Union[_sources_pb2.StreamSourceReference, _Mapping]] = ...,
        parse_info: _Optional[_Union[ParseInfo, _Mapping]] = ...,
        mode: _Optional[_Union[WindowMode, str]] = ...,
        environments: _Optional[_Iterable[str]] = ...,
        timeout_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        timestamp_attribute_name: _Optional[str] = ...,
        owner: _Optional[str] = ...,
        doc: _Optional[str] = ...,
        machine_type: _Optional[str] = ...,
        function: _Optional[_Union[FunctionReference, _Mapping]] = ...,
    ) -> None: ...

class StreamResolverParam(_message.Message):
    __slots__ = ["message", "message_window", "state"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    message: StreamResolverParamMessage
    message_window: StreamResolverParamMessageWindow
    state: ResolverState
    def __init__(
        self,
        message: _Optional[_Union[StreamResolverParamMessage, _Mapping]] = ...,
        message_window: _Optional[_Union[StreamResolverParamMessageWindow, _Mapping]] = ...,
        state: _Optional[_Union[ResolverState, _Mapping]] = ...,
    ) -> None: ...

class StreamResolverParamMessage(_message.Message):
    __slots__ = ["arrow_type", "name"]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    name: str
    def __init__(
        self, name: _Optional[str] = ..., arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...
    ) -> None: ...

class StreamResolverParamMessageWindow(_message.Message):
    __slots__ = ["arrow_type", "name"]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    name: str
    def __init__(
        self, name: _Optional[str] = ..., arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...
    ) -> None: ...

class StrictValidation(_message.Message):
    __slots__ = ["feature", "validations"]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
    feature: FeatureReference
    validations: _containers.RepeatedCompositeFieldContainer[FeatureValidation]
    def __init__(
        self,
        feature: _Optional[_Union[FeatureReference, _Mapping]] = ...,
        validations: _Optional[_Iterable[_Union[FeatureValidation, _Mapping]]] = ...,
    ) -> None: ...

class VersionInfo(_message.Message):
    __slots__ = ["default", "maximum"]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    default: int
    maximum: int
    def __init__(self, default: _Optional[int] = ..., maximum: _Optional[int] = ...) -> None: ...

class WindowInfo(_message.Message):
    __slots__ = ["duration"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class WindowedFeatureType(_message.Message):
    __slots__ = ["attribute_name", "is_autogenerated", "name", "namespace", "window_durations"]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOGENERATED_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WINDOW_DURATIONS_FIELD_NUMBER: _ClassVar[int]
    attribute_name: str
    is_autogenerated: bool
    name: str
    namespace: str
    window_durations: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    def __init__(
        self,
        name: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        is_autogenerated: bool = ...,
        window_durations: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ...,
        attribute_name: _Optional[str] = ...,
    ) -> None: ...

class ResolverKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class WindowMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
