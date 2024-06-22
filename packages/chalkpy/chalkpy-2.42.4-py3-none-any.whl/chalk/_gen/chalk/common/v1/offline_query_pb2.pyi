from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.common.v1 import chalk_error_pb2 as _chalk_error_pb2
from chalk._gen.chalk.expression.v1 import expression_pb2 as _expression_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ColumnMetadataList(_message.Message):
    __slots__ = ["metadata"]
    class ColumnMetadata(_message.Message):
        __slots__ = ["column_name", "dtype", "feature_fqn"]
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        DTYPE_FIELD_NUMBER: _ClassVar[int]
        FEATURE_FQN_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        dtype: str
        feature_fqn: str
        def __init__(
            self, feature_fqn: _Optional[str] = ..., column_name: _Optional[str] = ..., dtype: _Optional[str] = ...
        ) -> None: ...

    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.RepeatedCompositeFieldContainer[ColumnMetadataList.ColumnMetadata]
    def __init__(
        self, metadata: _Optional[_Iterable[_Union[ColumnMetadataList.ColumnMetadata, _Mapping]]] = ...
    ) -> None: ...

class GetOfflineQueryJobResponse(_message.Message):
    __slots__ = ["columns", "errors", "is_finished", "urls", "version"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    columns: ColumnMetadataList
    errors: _containers.RepeatedCompositeFieldContainer[_chalk_error_pb2.ChalkError]
    is_finished: bool
    urls: _containers.RepeatedScalarFieldContainer[str]
    version: int
    def __init__(
        self,
        is_finished: bool = ...,
        version: _Optional[int] = ...,
        urls: _Optional[_Iterable[str]] = ...,
        errors: _Optional[_Iterable[_Union[_chalk_error_pb2.ChalkError, _Mapping]]] = ...,
        columns: _Optional[_Union[ColumnMetadataList, _Mapping]] = ...,
    ) -> None: ...

class OfflineQueryExplain(_message.Message):
    __slots__ = ["only", "truthy"]
    class Only(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...

    ONLY_FIELD_NUMBER: _ClassVar[int]
    TRUTHY_FIELD_NUMBER: _ClassVar[int]
    only: OfflineQueryExplain.Only
    truthy: bool
    def __init__(
        self, truthy: bool = ..., only: _Optional[_Union[OfflineQueryExplain.Only, _Mapping]] = ...
    ) -> None: ...

class OfflineQueryInputs(_message.Message):
    __slots__ = ["feather_inputs", "no_inputs"]
    class NoInputs(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...

    FEATHER_INPUTS_FIELD_NUMBER: _ClassVar[int]
    NO_INPUTS_FIELD_NUMBER: _ClassVar[int]
    feather_inputs: bytes
    no_inputs: OfflineQueryInputs.NoInputs
    def __init__(
        self,
        feather_inputs: _Optional[bytes] = ...,
        no_inputs: _Optional[_Union[OfflineQueryInputs.NoInputs, _Mapping]] = ...,
    ) -> None: ...

class OfflineQueryRecomputeFeatures(_message.Message):
    __slots__ = ["all_or_none", "feature_list"]
    class FeatureList(_message.Message):
        __slots__ = ["feature_list"]
        FEATURE_LIST_FIELD_NUMBER: _ClassVar[int]
        feature_list: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, feature_list: _Optional[_Iterable[str]] = ...) -> None: ...

    ALL_OR_NONE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_LIST_FIELD_NUMBER: _ClassVar[int]
    all_or_none: bool
    feature_list: OfflineQueryRecomputeFeatures.FeatureList
    def __init__(
        self,
        all_or_none: bool = ...,
        feature_list: _Optional[_Union[OfflineQueryRecomputeFeatures.FeatureList, _Mapping]] = ...,
    ) -> None: ...

class OfflineQueryRequest(_message.Message):
    __slots__ = [
        "branch",
        "correlation_id",
        "dataset_name",
        "destination_format",
        "explain",
        "filters",
        "inputs",
        "max_cache_age_secs",
        "max_samples",
        "observed_at_lower_bound",
        "observed_at_upper_bound",
        "outputs",
        "recompute_features",
        "required_outputs",
        "store_plan_stages",
        "tags",
    ]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CACHE_AGE_SECS_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    RECOMPUTE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    STORE_PLAN_STAGES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    branch: str
    correlation_id: str
    dataset_name: str
    destination_format: str
    explain: OfflineQueryExplain
    filters: _containers.RepeatedCompositeFieldContainer[_expression_pb2.LogicalExprNode]
    inputs: OfflineQueryInputs
    max_cache_age_secs: int
    max_samples: int
    observed_at_lower_bound: str
    observed_at_upper_bound: str
    outputs: _containers.RepeatedScalarFieldContainer[str]
    recompute_features: OfflineQueryRecomputeFeatures
    required_outputs: _containers.RepeatedScalarFieldContainer[str]
    store_plan_stages: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        inputs: _Optional[_Union[OfflineQueryInputs, _Mapping]] = ...,
        outputs: _Optional[_Iterable[str]] = ...,
        required_outputs: _Optional[_Iterable[str]] = ...,
        destination_format: _Optional[str] = ...,
        branch: _Optional[str] = ...,
        dataset_name: _Optional[str] = ...,
        recompute_features: _Optional[_Union[OfflineQueryRecomputeFeatures, _Mapping]] = ...,
        store_plan_stages: bool = ...,
        filters: _Optional[_Iterable[_Union[_expression_pb2.LogicalExprNode, _Mapping]]] = ...,
        max_samples: _Optional[int] = ...,
        max_cache_age_secs: _Optional[int] = ...,
        explain: _Optional[_Union[OfflineQueryExplain, _Mapping]] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        correlation_id: _Optional[str] = ...,
        observed_at_lower_bound: _Optional[str] = ...,
        observed_at_upper_bound: _Optional[str] = ...,
    ) -> None: ...
