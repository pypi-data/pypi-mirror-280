from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

ALERT_SEVERITY_KIND_CRITICAL: AlertSeverityKind
ALERT_SEVERITY_KIND_ERROR: AlertSeverityKind
ALERT_SEVERITY_KIND_INFO: AlertSeverityKind
ALERT_SEVERITY_KIND_UNSPECIFIED: AlertSeverityKind
ALERT_SEVERITY_KIND_WARNING: AlertSeverityKind
CHART_LINK_KIND_FEATURE: ChartLinkKind
CHART_LINK_KIND_MANUAL: ChartLinkKind
CHART_LINK_KIND_QUERY: ChartLinkKind
CHART_LINK_KIND_RESOLVER: ChartLinkKind
CHART_LINK_KIND_UNSPECIFIED: ChartLinkKind
COMPARATOR_KIND_EQ: ComparatorKind
COMPARATOR_KIND_NEQ: ComparatorKind
COMPARATOR_KIND_ONE_OF: ComparatorKind
COMPARATOR_KIND_UNSPECIFIED: ComparatorKind
DESCRIPTOR: _descriptor.FileDescriptor
FILTER_KIND_CACHE_HIT: FilterKind
FILTER_KIND_CRON_STATUS: FilterKind
FILTER_KIND_FEATURE_NAME: FilterKind
FILTER_KIND_FEATURE_STATUS: FilterKind
FILTER_KIND_FEATURE_TAG: FilterKind
FILTER_KIND_IS_NULL: FilterKind
FILTER_KIND_MIGRATION_STATUS: FilterKind
FILTER_KIND_ONLINE_OFFLINE: FilterKind
FILTER_KIND_OPERATION_ID: FilterKind
FILTER_KIND_QUERY_NAME: FilterKind
FILTER_KIND_QUERY_STATUS: FilterKind
FILTER_KIND_RESOLVER_NAME: FilterKind
FILTER_KIND_RESOLVER_STATUS: FilterKind
FILTER_KIND_RESOLVER_TAG: FilterKind
FILTER_KIND_UNSPECIFIED: FilterKind
FILTER_KIND_USAGE_KIND: FilterKind
GROUP_BY_KIND_CACHE_HIT: GroupByKind
GROUP_BY_KIND_FEATURE_NAME: GroupByKind
GROUP_BY_KIND_FEATURE_STATUS: GroupByKind
GROUP_BY_KIND_IS_NULL: GroupByKind
GROUP_BY_KIND_ONLINE_OFFLINE: GroupByKind
GROUP_BY_KIND_QUERY_NAME: GroupByKind
GROUP_BY_KIND_QUERY_STATUS: GroupByKind
GROUP_BY_KIND_RESOLVER_NAME: GroupByKind
GROUP_BY_KIND_RESOLVER_STATUS: GroupByKind
GROUP_BY_KIND_UNSPECIFIED: GroupByKind
GROUP_BY_KIND_USAGE_KIND: GroupByKind
METRIC_FORMULA_KIND_ABS: MetricFormulaKind
METRIC_FORMULA_KIND_KS_STAT: MetricFormulaKind
METRIC_FORMULA_KIND_KS_TEST: MetricFormulaKind
METRIC_FORMULA_KIND_KS_THRESHOLD: MetricFormulaKind
METRIC_FORMULA_KIND_PRODUCT: MetricFormulaKind
METRIC_FORMULA_KIND_RATIO: MetricFormulaKind
METRIC_FORMULA_KIND_SUM: MetricFormulaKind
METRIC_FORMULA_KIND_TIME_OFFSET: MetricFormulaKind
METRIC_FORMULA_KIND_TOTAL_RATIO: MetricFormulaKind
METRIC_FORMULA_KIND_UNSPECIFIED: MetricFormulaKind
METRIC_KIND_BILLING_CRON: MetricKind
METRIC_KIND_BILLING_INFERENCE: MetricKind
METRIC_KIND_BILLING_MIGRATION: MetricKind
METRIC_KIND_CRON_COUNT: MetricKind
METRIC_KIND_CRON_LATENCY: MetricKind
METRIC_KIND_FEATURE_LATENCY: MetricKind
METRIC_KIND_FEATURE_NULL_RATIO: MetricKind
METRIC_KIND_FEATURE_REQUEST_COUNT: MetricKind
METRIC_KIND_FEATURE_STALENESS: MetricKind
METRIC_KIND_FEATURE_VALUE: MetricKind
METRIC_KIND_FEATURE_WRITE: MetricKind
METRIC_KIND_QUERY_COUNT: MetricKind
METRIC_KIND_QUERY_LATENCY: MetricKind
METRIC_KIND_QUERY_SUCCESS_RATIO: MetricKind
METRIC_KIND_RESOLVER_LATENCY: MetricKind
METRIC_KIND_RESOLVER_REQUEST_COUNT: MetricKind
METRIC_KIND_RESOLVER_SUCCESS_RATIO: MetricKind
METRIC_KIND_STREAM_MESSAGES_PROCESSED: MetricKind
METRIC_KIND_STREAM_MESSAGE_LATENCY: MetricKind
METRIC_KIND_STREAM_WINDOWS_PROCESSED: MetricKind
METRIC_KIND_STREAM_WINDOW_LATENCY: MetricKind
METRIC_KIND_UNSPECIFIED: MetricKind
THRESHOLD_KIND_ABOVE: ThresholdKind
THRESHOLD_KIND_BELOW: ThresholdKind
THRESHOLD_KIND_EQUAL: ThresholdKind
THRESHOLD_KIND_GREATER_EQUAL: ThresholdKind
THRESHOLD_KIND_LESS_EQUAL: ThresholdKind
THRESHOLD_KIND_NOT_EQUAL: ThresholdKind
THRESHOLD_KIND_UNSPECIFIED: ThresholdKind
WINDOW_FUNCTION_KIND_ALL_PERCENTILES: WindowFunctionKind
WINDOW_FUNCTION_KIND_COUNT: WindowFunctionKind
WINDOW_FUNCTION_KIND_MAX: WindowFunctionKind
WINDOW_FUNCTION_KIND_MEAN: WindowFunctionKind
WINDOW_FUNCTION_KIND_MIN: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_25: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_5: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_50: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_75: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_95: WindowFunctionKind
WINDOW_FUNCTION_KIND_PERCENTILE_99: WindowFunctionKind
WINDOW_FUNCTION_KIND_SUM: WindowFunctionKind
WINDOW_FUNCTION_KIND_UNSPECIFIED: WindowFunctionKind

class AlertTrigger(_message.Message):
    __slots__ = [
        "channel_name",
        "description",
        "name",
        "series_name",
        "severity",
        "threshold_position",
        "threshold_value",
    ]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIES_NAME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_POSITION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    channel_name: str
    description: str
    name: str
    series_name: str
    severity: AlertSeverityKind
    threshold_position: ThresholdKind
    threshold_value: float
    def __init__(
        self,
        name: _Optional[str] = ...,
        severity: _Optional[_Union[AlertSeverityKind, str]] = ...,
        threshold_position: _Optional[_Union[ThresholdKind, str]] = ...,
        threshold_value: _Optional[float] = ...,
        series_name: _Optional[str] = ...,
        channel_name: _Optional[str] = ...,
        description: _Optional[str] = ...,
    ) -> None: ...

class Chart(_message.Message):
    __slots__ = ["config", "entity_id", "entity_kind", "id"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_KIND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    config: MetricConfig
    entity_id: str
    entity_kind: ChartLinkKind
    id: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        config: _Optional[_Union[MetricConfig, _Mapping]] = ...,
        entity_kind: _Optional[_Union[ChartLinkKind, str]] = ...,
        entity_id: _Optional[str] = ...,
    ) -> None: ...

class DatasetFeatureOperand(_message.Message):
    __slots__ = ["dataset", "feature"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    feature: str
    def __init__(self, dataset: _Optional[str] = ..., feature: _Optional[str] = ...) -> None: ...

class MetricConfig(_message.Message):
    __slots__ = ["formulas", "name", "series", "trigger", "window_period"]
    FORMULAS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    WINDOW_PERIOD_FIELD_NUMBER: _ClassVar[int]
    formulas: _containers.RepeatedCompositeFieldContainer[MetricFormula]
    name: str
    series: _containers.RepeatedCompositeFieldContainer[MetricConfigSeries]
    trigger: AlertTrigger
    window_period: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        window_period: _Optional[str] = ...,
        series: _Optional[_Iterable[_Union[MetricConfigSeries, _Mapping]]] = ...,
        formulas: _Optional[_Iterable[_Union[MetricFormula, _Mapping]]] = ...,
        trigger: _Optional[_Union[AlertTrigger, _Mapping]] = ...,
    ) -> None: ...

class MetricConfigSeries(_message.Message):
    __slots__ = ["filters", "group_by", "metric", "name", "window_function"]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[MetricFilter]
    group_by: _containers.RepeatedScalarFieldContainer[GroupByKind]
    metric: MetricKind
    name: str
    window_function: WindowFunctionKind
    def __init__(
        self,
        metric: _Optional[_Union[MetricKind, str]] = ...,
        filters: _Optional[_Iterable[_Union[MetricFilter, _Mapping]]] = ...,
        name: _Optional[str] = ...,
        window_function: _Optional[_Union[WindowFunctionKind, str]] = ...,
        group_by: _Optional[_Iterable[_Union[GroupByKind, str]]] = ...,
    ) -> None: ...

class MetricFilter(_message.Message):
    __slots__ = ["comparator", "kind", "value"]
    COMPARATOR_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    comparator: ComparatorKind
    kind: FilterKind
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        kind: _Optional[_Union[FilterKind, str]] = ...,
        comparator: _Optional[_Union[ComparatorKind, str]] = ...,
        value: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class MetricFormula(_message.Message):
    __slots__ = ["dataset_feature_operands", "kind", "multi_series_operands", "name", "single_series_operands"]
    DATASET_FEATURE_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MULTI_SERIES_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SINGLE_SERIES_OPERANDS_FIELD_NUMBER: _ClassVar[int]
    dataset_feature_operands: DatasetFeatureOperand
    kind: MetricFormulaKind
    multi_series_operands: _containers.RepeatedScalarFieldContainer[int]
    name: str
    single_series_operands: int
    def __init__(
        self,
        kind: _Optional[_Union[MetricFormulaKind, str]] = ...,
        single_series_operands: _Optional[int] = ...,
        multi_series_operands: _Optional[_Iterable[int]] = ...,
        dataset_feature_operands: _Optional[_Union[DatasetFeatureOperand, _Mapping]] = ...,
        name: _Optional[str] = ...,
    ) -> None: ...

class MetricKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FilterKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ComparatorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class WindowFunctionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GroupByKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class MetricFormulaKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AlertSeverityKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ThresholdKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChartLinkKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
