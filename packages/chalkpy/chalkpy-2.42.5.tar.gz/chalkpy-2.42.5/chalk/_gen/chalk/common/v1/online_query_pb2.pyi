from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.common.v1 import chalk_error_pb2 as _chalk_error_pb2

DESCRIPTOR: _descriptor.FileDescriptor
FEATHER_BODY_TYPE_RECORD_BATCHES: FeatherBodyType
FEATHER_BODY_TYPE_TABLE: FeatherBodyType
FEATHER_BODY_TYPE_UNSPECIFIED: FeatherBodyType

class ExplainOptions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FeatureEncodingOptions(_message.Message):
    __slots__ = ["encode_structs_as_objects"]
    ENCODE_STRUCTS_AS_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    encode_structs_as_objects: bool
    def __init__(self, encode_structs_as_objects: bool = ...) -> None: ...

class FeatureMeta(_message.Message):
    __slots__ = ["cache_hit", "chosen_resolver_fqn", "primitive_type", "version"]
    CACHE_HIT_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_RESOLVER_FQN_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    cache_hit: bool
    chosen_resolver_fqn: str
    primitive_type: str
    version: int
    def __init__(
        self,
        chosen_resolver_fqn: _Optional[str] = ...,
        cache_hit: bool = ...,
        primitive_type: _Optional[str] = ...,
        version: _Optional[int] = ...,
    ) -> None: ...

class FeatureResult(_message.Message):
    __slots__ = ["error", "field", "meta", "pkey", "ts", "value"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    PKEY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    error: _chalk_error_pb2.ChalkError
    field: str
    meta: FeatureMeta
    pkey: _struct_pb2.Value
    ts: _timestamp_pb2.Timestamp
    value: _struct_pb2.Value
    def __init__(
        self,
        field: _Optional[str] = ...,
        pkey: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...,
        value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...,
        error: _Optional[_Union[_chalk_error_pb2.ChalkError, _Mapping]] = ...,
        ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        meta: _Optional[_Union[FeatureMeta, _Mapping]] = ...,
    ) -> None: ...

class GenericSingleQuery(_message.Message):
    __slots__ = ["bulk_request", "single_request"]
    BULK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SINGLE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    bulk_request: OnlineQueryBulkRequest
    single_request: OnlineQueryRequest
    def __init__(
        self,
        single_request: _Optional[_Union[OnlineQueryRequest, _Mapping]] = ...,
        bulk_request: _Optional[_Union[OnlineQueryBulkRequest, _Mapping]] = ...,
    ) -> None: ...

class GenericSingleResponse(_message.Message):
    __slots__ = ["bulk_response", "single_response"]
    BULK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    bulk_response: OnlineQueryBulkResponse
    single_response: OnlineQueryResponse
    def __init__(
        self,
        single_response: _Optional[_Union[OnlineQueryResponse, _Mapping]] = ...,
        bulk_response: _Optional[_Union[OnlineQueryBulkResponse, _Mapping]] = ...,
    ) -> None: ...

class OnlineQueryBulkRequest(_message.Message):
    __slots__ = ["body_type", "context", "inputs_feather", "now", "outputs", "response_options", "staleness"]
    class StalenessEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    BODY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FEATHER_FIELD_NUMBER: _ClassVar[int]
    NOW_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STALENESS_FIELD_NUMBER: _ClassVar[int]
    body_type: FeatherBodyType
    context: OnlineQueryContext
    inputs_feather: bytes
    now: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    outputs: _containers.RepeatedCompositeFieldContainer[OutputExpr]
    response_options: OnlineQueryResponseOptions
    staleness: _containers.ScalarMap[str, str]
    def __init__(
        self,
        inputs_feather: _Optional[bytes] = ...,
        outputs: _Optional[_Iterable[_Union[OutputExpr, _Mapping]]] = ...,
        now: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...,
        staleness: _Optional[_Mapping[str, str]] = ...,
        context: _Optional[_Union[OnlineQueryContext, _Mapping]] = ...,
        response_options: _Optional[_Union[OnlineQueryResponseOptions, _Mapping]] = ...,
        body_type: _Optional[_Union[FeatherBodyType, str]] = ...,
    ) -> None: ...

class OnlineQueryBulkResponse(_message.Message):
    __slots__ = ["errors", "groups_data", "response_meta", "scalars_data"]
    class GroupsDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

    ERRORS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    SCALARS_DATA_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_chalk_error_pb2.ChalkError]
    groups_data: _containers.ScalarMap[str, bytes]
    response_meta: OnlineQueryMetadata
    scalars_data: bytes
    def __init__(
        self,
        scalars_data: _Optional[bytes] = ...,
        groups_data: _Optional[_Mapping[str, bytes]] = ...,
        errors: _Optional[_Iterable[_Union[_chalk_error_pb2.ChalkError, _Mapping]]] = ...,
        response_meta: _Optional[_Union[OnlineQueryMetadata, _Mapping]] = ...,
    ) -> None: ...

class OnlineQueryContext(_message.Message):
    __slots__ = [
        "branch_id",
        "correlation_id",
        "deployment_id",
        "environment",
        "options",
        "query_name",
        "query_name_version",
        "required_resolver_tags",
        "tags",
    ]
    class OptionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...
        ) -> None: ...

    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_NAME_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_RESOLVER_TAGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    branch_id: str
    correlation_id: str
    deployment_id: str
    environment: str
    options: _containers.MessageMap[str, _struct_pb2.Value]
    query_name: str
    query_name_version: str
    required_resolver_tags: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        environment: _Optional[str] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        required_resolver_tags: _Optional[_Iterable[str]] = ...,
        deployment_id: _Optional[str] = ...,
        branch_id: _Optional[str] = ...,
        correlation_id: _Optional[str] = ...,
        query_name: _Optional[str] = ...,
        query_name_version: _Optional[str] = ...,
        options: _Optional[_Mapping[str, _struct_pb2.Value]] = ...,
    ) -> None: ...

class OnlineQueryMetadata(_message.Message):
    __slots__ = [
        "deployment_id",
        "environment_id",
        "environment_name",
        "execution_duration",
        "explain_output",
        "metadata",
        "query_hash",
        "query_id",
        "query_timestamp",
    ]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_HASH_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    deployment_id: str
    environment_id: str
    environment_name: str
    execution_duration: _duration_pb2.Duration
    explain_output: QueryExplainInfo
    metadata: _containers.ScalarMap[str, str]
    query_hash: str
    query_id: str
    query_timestamp: _timestamp_pb2.Timestamp
    def __init__(
        self,
        execution_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
        deployment_id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        environment_name: _Optional[str] = ...,
        query_id: _Optional[str] = ...,
        query_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        query_hash: _Optional[str] = ...,
        explain_output: _Optional[_Union[QueryExplainInfo, _Mapping]] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...

class OnlineQueryMultiRequest(_message.Message):
    __slots__ = ["queries"]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    queries: _containers.RepeatedCompositeFieldContainer[GenericSingleQuery]
    def __init__(self, queries: _Optional[_Iterable[_Union[GenericSingleQuery, _Mapping]]] = ...) -> None: ...

class OnlineQueryMultiResponse(_message.Message):
    __slots__ = ["errors", "responses"]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_chalk_error_pb2.ChalkError]
    responses: _containers.RepeatedCompositeFieldContainer[GenericSingleResponse]
    def __init__(
        self,
        responses: _Optional[_Iterable[_Union[GenericSingleResponse, _Mapping]]] = ...,
        errors: _Optional[_Iterable[_Union[_chalk_error_pb2.ChalkError, _Mapping]]] = ...,
    ) -> None: ...

class OnlineQueryRequest(_message.Message):
    __slots__ = ["context", "inputs", "now", "outputs", "response_options", "staleness"]
    class InputsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...
        ) -> None: ...

    class StalenessEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    NOW_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STALENESS_FIELD_NUMBER: _ClassVar[int]
    context: OnlineQueryContext
    inputs: _containers.MessageMap[str, _struct_pb2.Value]
    now: _timestamp_pb2.Timestamp
    outputs: _containers.RepeatedCompositeFieldContainer[OutputExpr]
    response_options: OnlineQueryResponseOptions
    staleness: _containers.ScalarMap[str, str]
    def __init__(
        self,
        inputs: _Optional[_Mapping[str, _struct_pb2.Value]] = ...,
        outputs: _Optional[_Iterable[_Union[OutputExpr, _Mapping]]] = ...,
        now: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        staleness: _Optional[_Mapping[str, str]] = ...,
        context: _Optional[_Union[OnlineQueryContext, _Mapping]] = ...,
        response_options: _Optional[_Union[OnlineQueryResponseOptions, _Mapping]] = ...,
    ) -> None: ...

class OnlineQueryResponse(_message.Message):
    __slots__ = ["data", "errors", "response_meta"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_META_FIELD_NUMBER: _ClassVar[int]
    data: OnlineQueryResult
    errors: _containers.RepeatedCompositeFieldContainer[_chalk_error_pb2.ChalkError]
    response_meta: OnlineQueryMetadata
    def __init__(
        self,
        data: _Optional[_Union[OnlineQueryResult, _Mapping]] = ...,
        errors: _Optional[_Iterable[_Union[_chalk_error_pb2.ChalkError, _Mapping]]] = ...,
        response_meta: _Optional[_Union[OnlineQueryMetadata, _Mapping]] = ...,
    ) -> None: ...

class OnlineQueryResponseOptions(_message.Message):
    __slots__ = ["encoding_options", "explain", "include_meta", "metadata"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    ENCODING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_META_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    encoding_options: FeatureEncodingOptions
    explain: ExplainOptions
    include_meta: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        include_meta: bool = ...,
        explain: _Optional[_Union[ExplainOptions, _Mapping]] = ...,
        encoding_options: _Optional[_Union[FeatureEncodingOptions, _Mapping]] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...

class OnlineQueryResult(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[FeatureResult]
    def __init__(self, results: _Optional[_Iterable[_Union[FeatureResult, _Mapping]]] = ...) -> None: ...

class OutputExpr(_message.Message):
    __slots__ = ["feature_fqn"]
    FEATURE_FQN_FIELD_NUMBER: _ClassVar[int]
    feature_fqn: str
    def __init__(self, feature_fqn: _Optional[str] = ...) -> None: ...

class QueryExplainInfo(_message.Message):
    __slots__ = ["plan_string"]
    PLAN_STRING_FIELD_NUMBER: _ClassVar[int]
    plan_string: str
    def __init__(self, plan_string: _Optional[str] = ...) -> None: ...

class FeatherBodyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
