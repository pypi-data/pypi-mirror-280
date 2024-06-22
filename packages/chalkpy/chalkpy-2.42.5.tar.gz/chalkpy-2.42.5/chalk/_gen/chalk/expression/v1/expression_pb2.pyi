from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.arrow.v1 import arrow_pb2 as _arrow_pb2

AGGREGATE_FUNCTION_APPROX_DISTINCT: AggregateFunction
AGGREGATE_FUNCTION_APPROX_MEDIAN: AggregateFunction
AGGREGATE_FUNCTION_APPROX_PERCENTILE_CONT: AggregateFunction
AGGREGATE_FUNCTION_APPROX_PERCENTILE_CONT_WITH_WEIGHT: AggregateFunction
AGGREGATE_FUNCTION_ARRAY: AggregateFunction
AGGREGATE_FUNCTION_AVG: AggregateFunction
AGGREGATE_FUNCTION_BIT_AND: AggregateFunction
AGGREGATE_FUNCTION_BIT_OR: AggregateFunction
AGGREGATE_FUNCTION_BIT_XOR: AggregateFunction
AGGREGATE_FUNCTION_BOOL_AND: AggregateFunction
AGGREGATE_FUNCTION_BOOL_OR: AggregateFunction
AGGREGATE_FUNCTION_CORRELATION: AggregateFunction
AGGREGATE_FUNCTION_COUNT: AggregateFunction
AGGREGATE_FUNCTION_COVARIANCE: AggregateFunction
AGGREGATE_FUNCTION_COVARIANCE_POP: AggregateFunction
AGGREGATE_FUNCTION_FIRST_VALUE: AggregateFunction
AGGREGATE_FUNCTION_GROUPING: AggregateFunction
AGGREGATE_FUNCTION_LAST_VALUE: AggregateFunction
AGGREGATE_FUNCTION_MAX: AggregateFunction
AGGREGATE_FUNCTION_MEDIAN: AggregateFunction
AGGREGATE_FUNCTION_MIN: AggregateFunction
AGGREGATE_FUNCTION_REGR_AVGX: AggregateFunction
AGGREGATE_FUNCTION_REGR_AVGY: AggregateFunction
AGGREGATE_FUNCTION_REGR_COUNT: AggregateFunction
AGGREGATE_FUNCTION_REGR_INTERCEPT: AggregateFunction
AGGREGATE_FUNCTION_REGR_R2: AggregateFunction
AGGREGATE_FUNCTION_REGR_SLOPE: AggregateFunction
AGGREGATE_FUNCTION_REGR_SXX: AggregateFunction
AGGREGATE_FUNCTION_REGR_SXY: AggregateFunction
AGGREGATE_FUNCTION_REGR_SYY: AggregateFunction
AGGREGATE_FUNCTION_STDDEV: AggregateFunction
AGGREGATE_FUNCTION_STDDEV_POP: AggregateFunction
AGGREGATE_FUNCTION_STRING: AggregateFunction
AGGREGATE_FUNCTION_SUM: AggregateFunction
AGGREGATE_FUNCTION_UNSPECIFIED: AggregateFunction
AGGREGATE_FUNCTION_VARIANCE: AggregateFunction
AGGREGATE_FUNCTION_VARIANCE_POP: AggregateFunction
BUILT_IN_WINDOW_FUNCTION_CUME_DIST: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_DENSE_RANK: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_FIRST_VALUE: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_LAG: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_LAST_VALUE: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_LEAD: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_NTH_VALUE: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_NTILE: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_PERCENT_RANK: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_RANK: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_ROW_NUMBER: BuiltInWindowFunction
BUILT_IN_WINDOW_FUNCTION_UNSPECIFIED: BuiltInWindowFunction
DESCRIPTOR: _descriptor.FileDescriptor
SCALAR_FUNCTION_ABS: ScalarFunction
SCALAR_FUNCTION_ACOS: ScalarFunction
SCALAR_FUNCTION_ACOSH: ScalarFunction
SCALAR_FUNCTION_ARRAY: ScalarFunction
SCALAR_FUNCTION_ARRAY_APPEND: ScalarFunction
SCALAR_FUNCTION_ARRAY_CONCAT: ScalarFunction
SCALAR_FUNCTION_ARRAY_DIMS: ScalarFunction
SCALAR_FUNCTION_ARRAY_DISTINCT: ScalarFunction
SCALAR_FUNCTION_ARRAY_ELEMENT: ScalarFunction
SCALAR_FUNCTION_ARRAY_EMPTY: ScalarFunction
SCALAR_FUNCTION_ARRAY_EXCEPT: ScalarFunction
SCALAR_FUNCTION_ARRAY_HAS: ScalarFunction
SCALAR_FUNCTION_ARRAY_HAS_ALL: ScalarFunction
SCALAR_FUNCTION_ARRAY_HAS_ANY: ScalarFunction
SCALAR_FUNCTION_ARRAY_INTERSECT: ScalarFunction
SCALAR_FUNCTION_ARRAY_LENGTH: ScalarFunction
SCALAR_FUNCTION_ARRAY_NDIMS: ScalarFunction
SCALAR_FUNCTION_ARRAY_POP_BACK: ScalarFunction
SCALAR_FUNCTION_ARRAY_POP_FRONT: ScalarFunction
SCALAR_FUNCTION_ARRAY_POSITION: ScalarFunction
SCALAR_FUNCTION_ARRAY_POSITIONS: ScalarFunction
SCALAR_FUNCTION_ARRAY_PREPEND: ScalarFunction
SCALAR_FUNCTION_ARRAY_REMOVE: ScalarFunction
SCALAR_FUNCTION_ARRAY_REMOVE_ALL: ScalarFunction
SCALAR_FUNCTION_ARRAY_REMOVE_N: ScalarFunction
SCALAR_FUNCTION_ARRAY_REPEAT: ScalarFunction
SCALAR_FUNCTION_ARRAY_REPLACE: ScalarFunction
SCALAR_FUNCTION_ARRAY_REPLACE_ALL: ScalarFunction
SCALAR_FUNCTION_ARRAY_REPLACE_N: ScalarFunction
SCALAR_FUNCTION_ARRAY_SLICE: ScalarFunction
SCALAR_FUNCTION_ARRAY_SORT: ScalarFunction
SCALAR_FUNCTION_ARRAY_TO_STRING: ScalarFunction
SCALAR_FUNCTION_ARRAY_UNION: ScalarFunction
SCALAR_FUNCTION_ARROW_TYPEOF: ScalarFunction
SCALAR_FUNCTION_ASCII: ScalarFunction
SCALAR_FUNCTION_ASIN: ScalarFunction
SCALAR_FUNCTION_ASINH: ScalarFunction
SCALAR_FUNCTION_ATAN: ScalarFunction
SCALAR_FUNCTION_ATAN2: ScalarFunction
SCALAR_FUNCTION_ATANH: ScalarFunction
SCALAR_FUNCTION_BIT_LENGTH: ScalarFunction
SCALAR_FUNCTION_BTRIM: ScalarFunction
SCALAR_FUNCTION_CARDINALITY: ScalarFunction
SCALAR_FUNCTION_CBRT: ScalarFunction
SCALAR_FUNCTION_CEIL: ScalarFunction
SCALAR_FUNCTION_CHARACTER_LENGTH: ScalarFunction
SCALAR_FUNCTION_CHR: ScalarFunction
SCALAR_FUNCTION_COALESCE: ScalarFunction
SCALAR_FUNCTION_CONCAT: ScalarFunction
SCALAR_FUNCTION_CONCAT_WITH_SEPARATOR: ScalarFunction
SCALAR_FUNCTION_COS: ScalarFunction
SCALAR_FUNCTION_COSH: ScalarFunction
SCALAR_FUNCTION_COT: ScalarFunction
SCALAR_FUNCTION_CURRENT_DATE: ScalarFunction
SCALAR_FUNCTION_CURRENT_TIME: ScalarFunction
SCALAR_FUNCTION_DATE_BIN: ScalarFunction
SCALAR_FUNCTION_DATE_PART: ScalarFunction
SCALAR_FUNCTION_DATE_TRUNC: ScalarFunction
SCALAR_FUNCTION_DECODE: ScalarFunction
SCALAR_FUNCTION_DEGREES: ScalarFunction
SCALAR_FUNCTION_DIGEST: ScalarFunction
SCALAR_FUNCTION_ENCODE: ScalarFunction
SCALAR_FUNCTION_EXP: ScalarFunction
SCALAR_FUNCTION_FACTORIAL: ScalarFunction
SCALAR_FUNCTION_FIND_IN_SET: ScalarFunction
SCALAR_FUNCTION_FLATTEN: ScalarFunction
SCALAR_FUNCTION_FLOOR: ScalarFunction
SCALAR_FUNCTION_FROM_UNIXTIME: ScalarFunction
SCALAR_FUNCTION_GCD: ScalarFunction
SCALAR_FUNCTION_INIT_CAP: ScalarFunction
SCALAR_FUNCTION_ISNAN: ScalarFunction
SCALAR_FUNCTION_ISZERO: ScalarFunction
SCALAR_FUNCTION_LCM: ScalarFunction
SCALAR_FUNCTION_LEFT: ScalarFunction
SCALAR_FUNCTION_LEVENSHTEIN: ScalarFunction
SCALAR_FUNCTION_LN: ScalarFunction
SCALAR_FUNCTION_LOG: ScalarFunction
SCALAR_FUNCTION_LOG10: ScalarFunction
SCALAR_FUNCTION_LOG2: ScalarFunction
SCALAR_FUNCTION_LOWER: ScalarFunction
SCALAR_FUNCTION_LPAD: ScalarFunction
SCALAR_FUNCTION_LTRIM: ScalarFunction
SCALAR_FUNCTION_MD5: ScalarFunction
SCALAR_FUNCTION_NANVL: ScalarFunction
SCALAR_FUNCTION_NOW: ScalarFunction
SCALAR_FUNCTION_NULL_IF: ScalarFunction
SCALAR_FUNCTION_OCTET_LENGTH: ScalarFunction
SCALAR_FUNCTION_OVER_LAY: ScalarFunction
SCALAR_FUNCTION_PI: ScalarFunction
SCALAR_FUNCTION_POWER: ScalarFunction
SCALAR_FUNCTION_RADIANS: ScalarFunction
SCALAR_FUNCTION_RANDOM: ScalarFunction
SCALAR_FUNCTION_RANGE: ScalarFunction
SCALAR_FUNCTION_REGEXP_MATCH: ScalarFunction
SCALAR_FUNCTION_REGEXP_REPLACE: ScalarFunction
SCALAR_FUNCTION_REPEAT: ScalarFunction
SCALAR_FUNCTION_REPLACE: ScalarFunction
SCALAR_FUNCTION_REVERSE: ScalarFunction
SCALAR_FUNCTION_RIGHT: ScalarFunction
SCALAR_FUNCTION_ROUND: ScalarFunction
SCALAR_FUNCTION_RPAD: ScalarFunction
SCALAR_FUNCTION_RTRIM: ScalarFunction
SCALAR_FUNCTION_SHA224: ScalarFunction
SCALAR_FUNCTION_SHA256: ScalarFunction
SCALAR_FUNCTION_SHA384: ScalarFunction
SCALAR_FUNCTION_SHA512: ScalarFunction
SCALAR_FUNCTION_SIGNUM: ScalarFunction
SCALAR_FUNCTION_SIN: ScalarFunction
SCALAR_FUNCTION_SINH: ScalarFunction
SCALAR_FUNCTION_SPLIT_PART: ScalarFunction
SCALAR_FUNCTION_SQRT: ScalarFunction
SCALAR_FUNCTION_STARTS_WITH: ScalarFunction
SCALAR_FUNCTION_STRING_TO_ARRAY: ScalarFunction
SCALAR_FUNCTION_STRPOS: ScalarFunction
SCALAR_FUNCTION_STRUCT_FUN: ScalarFunction
SCALAR_FUNCTION_SUBSTR: ScalarFunction
SCALAR_FUNCTION_SUBSTR_INDEX: ScalarFunction
SCALAR_FUNCTION_TAN: ScalarFunction
SCALAR_FUNCTION_TANH: ScalarFunction
SCALAR_FUNCTION_TO_HEX: ScalarFunction
SCALAR_FUNCTION_TO_TIMESTAMP: ScalarFunction
SCALAR_FUNCTION_TO_TIMESTAMP_MICROS: ScalarFunction
SCALAR_FUNCTION_TO_TIMESTAMP_MILLIS: ScalarFunction
SCALAR_FUNCTION_TO_TIMESTAMP_NANOS: ScalarFunction
SCALAR_FUNCTION_TO_TIMESTAMP_SECONDS: ScalarFunction
SCALAR_FUNCTION_TRANSLATE: ScalarFunction
SCALAR_FUNCTION_TRIM: ScalarFunction
SCALAR_FUNCTION_TRUNC: ScalarFunction
SCALAR_FUNCTION_UNSPECIFIED: ScalarFunction
SCALAR_FUNCTION_UPPER: ScalarFunction
SCALAR_FUNCTION_UUID: ScalarFunction
WINDOW_FRAME_BOUND_TYPE_CURRENT_ROW: WindowFrameBoundType
WINDOW_FRAME_BOUND_TYPE_FOLLOWING: WindowFrameBoundType
WINDOW_FRAME_BOUND_TYPE_PRECEDING: WindowFrameBoundType
WINDOW_FRAME_BOUND_TYPE_UNSPECIFIED: WindowFrameBoundType
WINDOW_FRAME_UNITS_GROUPS: WindowFrameUnits
WINDOW_FRAME_UNITS_RANGE: WindowFrameUnits
WINDOW_FRAME_UNITS_ROWS: WindowFrameUnits
WINDOW_FRAME_UNITS_UNSPECIFIED: WindowFrameUnits

class AggregateExprNode(_message.Message):
    __slots__ = ["aggr_function", "distinct", "expr", "filter", "order_by"]
    AGGR_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    aggr_function: AggregateFunction
    distinct: bool
    expr: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    filter: LogicalExprNode
    order_by: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(
        self,
        aggr_function: _Optional[_Union[AggregateFunction, str]] = ...,
        expr: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
        distinct: bool = ...,
        filter: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        order_by: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
    ) -> None: ...

class AggregateUDFExprNode(_message.Message):
    __slots__ = ["args", "filter", "fun_name", "order_by"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FUN_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    filter: LogicalExprNode
    fun_name: str
    order_by: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(
        self,
        fun_name: _Optional[str] = ...,
        args: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
        filter: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        order_by: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
    ) -> None: ...

class AliasNode(_message.Message):
    __slots__ = ["alias", "expr", "relation"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    alias: str
    expr: LogicalExprNode
    relation: _containers.RepeatedCompositeFieldContainer[OwnedTableReference]
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        alias: _Optional[str] = ...,
        relation: _Optional[_Iterable[_Union[OwnedTableReference, _Mapping]]] = ...,
    ) -> None: ...

class BareTableReference(_message.Message):
    __slots__ = ["table"]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    table: str
    def __init__(self, table: _Optional[str] = ...) -> None: ...

class BetweenNode(_message.Message):
    __slots__ = ["expr", "high", "low", "negated"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    high: LogicalExprNode
    low: LogicalExprNode
    negated: bool
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        negated: bool = ...,
        low: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        high: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
    ) -> None: ...

class BinaryExprNode(_message.Message):
    __slots__ = ["op", "operands"]
    OPERANDS_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    op: str
    operands: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(
        self, operands: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ..., op: _Optional[str] = ...
    ) -> None: ...

class CaseNode(_message.Message):
    __slots__ = ["else_expr", "expr", "when_then_expr"]
    ELSE_EXPR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    WHEN_THEN_EXPR_FIELD_NUMBER: _ClassVar[int]
    else_expr: LogicalExprNode
    expr: LogicalExprNode
    when_then_expr: _containers.RepeatedCompositeFieldContainer[WhenThen]
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        when_then_expr: _Optional[_Iterable[_Union[WhenThen, _Mapping]]] = ...,
        else_expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
    ) -> None: ...

class CastNode(_message.Message):
    __slots__ = ["arrow_type", "expr"]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    expr: LogicalExprNode
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
    ) -> None: ...

class Column(_message.Message):
    __slots__ = ["name", "relation"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    relation: ColumnRelation
    def __init__(
        self, name: _Optional[str] = ..., relation: _Optional[_Union[ColumnRelation, _Mapping]] = ...
    ) -> None: ...

class ColumnRelation(_message.Message):
    __slots__ = ["relation"]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    relation: str
    def __init__(self, relation: _Optional[str] = ...) -> None: ...

class CubeNode(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(self, expr: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...) -> None: ...

class FullTableReference(_message.Message):
    __slots__ = ["catalog", "schema", "table"]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    catalog: str
    schema: str
    table: str
    def __init__(
        self, catalog: _Optional[str] = ..., schema: _Optional[str] = ..., table: _Optional[str] = ...
    ) -> None: ...

class GetIndexedField(_message.Message):
    __slots__ = ["expr", "list_index", "list_range", "named_struct_field"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    LIST_INDEX_FIELD_NUMBER: _ClassVar[int]
    LIST_RANGE_FIELD_NUMBER: _ClassVar[int]
    NAMED_STRUCT_FIELD_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    list_index: ListIndex
    list_range: ListRange
    named_struct_field: NamedStructField
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        named_struct_field: _Optional[_Union[NamedStructField, _Mapping]] = ...,
        list_index: _Optional[_Union[ListIndex, _Mapping]] = ...,
        list_range: _Optional[_Union[ListRange, _Mapping]] = ...,
    ) -> None: ...

class GroupingSetNode(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: _containers.RepeatedCompositeFieldContainer[LogicalExprList]
    def __init__(self, expr: _Optional[_Iterable[_Union[LogicalExprList, _Mapping]]] = ...) -> None: ...

class ILikeNode(_message.Message):
    __slots__ = ["escape_char", "expr", "negated", "pattern"]
    ESCAPE_CHAR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    escape_char: str
    expr: LogicalExprNode
    negated: bool
    pattern: LogicalExprNode
    def __init__(
        self,
        negated: bool = ...,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        pattern: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        escape_char: _Optional[str] = ...,
    ) -> None: ...

class InListNode(_message.Message):
    __slots__ = ["expr", "list", "negated"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    list: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    negated: bool
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        list: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
        negated: bool = ...,
    ) -> None: ...

class IsFalse(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsNotFalse(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsNotNull(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsNotTrue(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsNotUnknown(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsNull(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsTrue(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class IsUnknown(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class LikeNode(_message.Message):
    __slots__ = ["escape_char", "expr", "negated", "pattern"]
    ESCAPE_CHAR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    escape_char: str
    expr: LogicalExprNode
    negated: bool
    pattern: LogicalExprNode
    def __init__(
        self,
        negated: bool = ...,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        pattern: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        escape_char: _Optional[str] = ...,
    ) -> None: ...

class ListIndex(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: LogicalExprNode
    def __init__(self, key: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class ListRange(_message.Message):
    __slots__ = ["start", "stop"]
    START_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    start: LogicalExprNode
    stop: LogicalExprNode
    def __init__(
        self,
        start: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        stop: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
    ) -> None: ...

class LogicalExprList(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(self, expr: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...) -> None: ...

class LogicalExprNode(_message.Message):
    __slots__ = [
        "aggregate_expr",
        "aggregate_udf_expr",
        "alias",
        "between",
        "binary_expr",
        "case",
        "cast",
        "column",
        "cube",
        "get_indexed_field",
        "grouping_set",
        "ilike",
        "in_list",
        "is_false",
        "is_not_false",
        "is_not_null_expr",
        "is_not_true",
        "is_not_unknown",
        "is_null_expr",
        "is_true",
        "is_unknown",
        "like",
        "literal",
        "negative",
        "not_expr",
        "placeholder",
        "rollup",
        "scalar_function",
        "scalar_udf_expr",
        "similar_to",
        "sort",
        "try_cast",
        "wildcard",
        "window_expr",
    ]
    AGGREGATE_EXPR_FIELD_NUMBER: _ClassVar[int]
    AGGREGATE_UDF_EXPR_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FIELD_NUMBER: _ClassVar[int]
    BINARY_EXPR_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    CAST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    CUBE_FIELD_NUMBER: _ClassVar[int]
    GET_INDEXED_FIELD_FIELD_NUMBER: _ClassVar[int]
    GROUPING_SET_FIELD_NUMBER: _ClassVar[int]
    ILIKE_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_FALSE_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_FALSE_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_NULL_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_TRUE_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    IS_NULL_EXPR_FIELD_NUMBER: _ClassVar[int]
    IS_TRUE_FIELD_NUMBER: _ClassVar[int]
    IS_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    LITERAL_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPR_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    ROLLUP_FIELD_NUMBER: _ClassVar[int]
    SCALAR_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    SCALAR_UDF_EXPR_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_TO_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TRY_CAST_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_FIELD_NUMBER: _ClassVar[int]
    WINDOW_EXPR_FIELD_NUMBER: _ClassVar[int]
    aggregate_expr: AggregateExprNode
    aggregate_udf_expr: AggregateUDFExprNode
    alias: AliasNode
    between: BetweenNode
    binary_expr: BinaryExprNode
    case: CaseNode
    cast: CastNode
    column: Column
    cube: CubeNode
    get_indexed_field: GetIndexedField
    grouping_set: GroupingSetNode
    ilike: ILikeNode
    in_list: InListNode
    is_false: IsFalse
    is_not_false: IsNotFalse
    is_not_null_expr: IsNotNull
    is_not_true: IsNotTrue
    is_not_unknown: IsNotUnknown
    is_null_expr: IsNull
    is_true: IsTrue
    is_unknown: IsUnknown
    like: LikeNode
    literal: _arrow_pb2.ScalarValue
    negative: NegativeNode
    not_expr: Not
    placeholder: PlaceholderNode
    rollup: RollupNode
    scalar_function: ScalarFunctionNode
    scalar_udf_expr: ScalarUDFExprNode
    similar_to: SimilarToNode
    sort: SortExprNode
    try_cast: TryCastNode
    wildcard: Wildcard
    window_expr: WindowExprNode
    def __init__(
        self,
        column: _Optional[_Union[Column, _Mapping]] = ...,
        alias: _Optional[_Union[AliasNode, _Mapping]] = ...,
        literal: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...,
        binary_expr: _Optional[_Union[BinaryExprNode, _Mapping]] = ...,
        aggregate_expr: _Optional[_Union[AggregateExprNode, _Mapping]] = ...,
        is_null_expr: _Optional[_Union[IsNull, _Mapping]] = ...,
        is_not_null_expr: _Optional[_Union[IsNotNull, _Mapping]] = ...,
        not_expr: _Optional[_Union[Not, _Mapping]] = ...,
        between: _Optional[_Union[BetweenNode, _Mapping]] = ...,
        case: _Optional[_Union[CaseNode, _Mapping]] = ...,
        cast: _Optional[_Union[CastNode, _Mapping]] = ...,
        sort: _Optional[_Union[SortExprNode, _Mapping]] = ...,
        negative: _Optional[_Union[NegativeNode, _Mapping]] = ...,
        in_list: _Optional[_Union[InListNode, _Mapping]] = ...,
        wildcard: _Optional[_Union[Wildcard, _Mapping]] = ...,
        scalar_function: _Optional[_Union[ScalarFunctionNode, _Mapping]] = ...,
        try_cast: _Optional[_Union[TryCastNode, _Mapping]] = ...,
        window_expr: _Optional[_Union[WindowExprNode, _Mapping]] = ...,
        aggregate_udf_expr: _Optional[_Union[AggregateUDFExprNode, _Mapping]] = ...,
        scalar_udf_expr: _Optional[_Union[ScalarUDFExprNode, _Mapping]] = ...,
        get_indexed_field: _Optional[_Union[GetIndexedField, _Mapping]] = ...,
        grouping_set: _Optional[_Union[GroupingSetNode, _Mapping]] = ...,
        cube: _Optional[_Union[CubeNode, _Mapping]] = ...,
        rollup: _Optional[_Union[RollupNode, _Mapping]] = ...,
        is_true: _Optional[_Union[IsTrue, _Mapping]] = ...,
        is_false: _Optional[_Union[IsFalse, _Mapping]] = ...,
        is_unknown: _Optional[_Union[IsUnknown, _Mapping]] = ...,
        is_not_true: _Optional[_Union[IsNotTrue, _Mapping]] = ...,
        is_not_false: _Optional[_Union[IsNotFalse, _Mapping]] = ...,
        is_not_unknown: _Optional[_Union[IsNotUnknown, _Mapping]] = ...,
        like: _Optional[_Union[LikeNode, _Mapping]] = ...,
        ilike: _Optional[_Union[ILikeNode, _Mapping]] = ...,
        similar_to: _Optional[_Union[SimilarToNode, _Mapping]] = ...,
        placeholder: _Optional[_Union[PlaceholderNode, _Mapping]] = ...,
    ) -> None: ...

class NamedStructField(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: _arrow_pb2.ScalarValue
    def __init__(self, name: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...) -> None: ...

class NegativeNode(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class Not(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: LogicalExprNode
    def __init__(self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...) -> None: ...

class OwnedTableReference(_message.Message):
    __slots__ = ["bare", "full", "partial"]
    BARE_FIELD_NUMBER: _ClassVar[int]
    FULL_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    bare: BareTableReference
    full: FullTableReference
    partial: PartialTableReference
    def __init__(
        self,
        bare: _Optional[_Union[BareTableReference, _Mapping]] = ...,
        partial: _Optional[_Union[PartialTableReference, _Mapping]] = ...,
        full: _Optional[_Union[FullTableReference, _Mapping]] = ...,
    ) -> None: ...

class PartialTableReference(_message.Message):
    __slots__ = ["schema", "table"]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...

class PlaceholderNode(_message.Message):
    __slots__ = ["data_type", "id"]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    data_type: _arrow_pb2.ArrowType
    id: str
    def __init__(
        self, id: _Optional[str] = ..., data_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...
    ) -> None: ...

class RollupNode(_message.Message):
    __slots__ = ["expr"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    expr: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    def __init__(self, expr: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...) -> None: ...

class ScalarFunctionNode(_message.Message):
    __slots__ = ["args", "fun"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FUN_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    fun: ScalarFunction
    def __init__(
        self,
        fun: _Optional[_Union[ScalarFunction, str]] = ...,
        args: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
    ) -> None: ...

class ScalarUDFExprNode(_message.Message):
    __slots__ = ["args", "fun_name"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    FUN_NAME_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    fun_name: str
    def __init__(
        self, fun_name: _Optional[str] = ..., args: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...
    ) -> None: ...

class SimilarToNode(_message.Message):
    __slots__ = ["escape_char", "expr", "negated", "pattern"]
    ESCAPE_CHAR_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    escape_char: str
    expr: LogicalExprNode
    negated: bool
    pattern: LogicalExprNode
    def __init__(
        self,
        negated: bool = ...,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        pattern: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        escape_char: _Optional[str] = ...,
    ) -> None: ...

class SortExprNode(_message.Message):
    __slots__ = ["asc", "expr", "nulls_first"]
    ASC_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    NULLS_FIRST_FIELD_NUMBER: _ClassVar[int]
    asc: bool
    expr: LogicalExprNode
    nulls_first: bool
    def __init__(
        self, expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ..., asc: bool = ..., nulls_first: bool = ...
    ) -> None: ...

class TryCastNode(_message.Message):
    __slots__ = ["arrow_type", "expr"]
    ARROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    arrow_type: _arrow_pb2.ArrowType
    expr: LogicalExprNode
    def __init__(
        self,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        arrow_type: _Optional[_Union[_arrow_pb2.ArrowType, _Mapping]] = ...,
    ) -> None: ...

class WhenThen(_message.Message):
    __slots__ = ["then_expr", "when_expr"]
    THEN_EXPR_FIELD_NUMBER: _ClassVar[int]
    WHEN_EXPR_FIELD_NUMBER: _ClassVar[int]
    then_expr: LogicalExprNode
    when_expr: LogicalExprNode
    def __init__(
        self,
        when_expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        then_expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
    ) -> None: ...

class Wildcard(_message.Message):
    __slots__ = ["qualifier"]
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    qualifier: str
    def __init__(self, qualifier: _Optional[str] = ...) -> None: ...

class WindowExprNode(_message.Message):
    __slots__ = [
        "aggr_function",
        "built_in_function",
        "expr",
        "order_by",
        "partition_by",
        "udaf",
        "udwf",
        "window_frame",
    ]
    AGGR_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    BUILT_IN_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_BY_FIELD_NUMBER: _ClassVar[int]
    UDAF_FIELD_NUMBER: _ClassVar[int]
    UDWF_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FRAME_FIELD_NUMBER: _ClassVar[int]
    aggr_function: AggregateFunction
    built_in_function: BuiltInWindowFunction
    expr: LogicalExprNode
    order_by: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    partition_by: _containers.RepeatedCompositeFieldContainer[LogicalExprNode]
    udaf: str
    udwf: str
    window_frame: WindowFrame
    def __init__(
        self,
        aggr_function: _Optional[_Union[AggregateFunction, str]] = ...,
        built_in_function: _Optional[_Union[BuiltInWindowFunction, str]] = ...,
        udaf: _Optional[str] = ...,
        udwf: _Optional[str] = ...,
        expr: _Optional[_Union[LogicalExprNode, _Mapping]] = ...,
        partition_by: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
        order_by: _Optional[_Iterable[_Union[LogicalExprNode, _Mapping]]] = ...,
        window_frame: _Optional[_Union[WindowFrame, _Mapping]] = ...,
    ) -> None: ...

class WindowFrame(_message.Message):
    __slots__ = ["bound", "start_bound", "window_frame_units"]
    BOUND_FIELD_NUMBER: _ClassVar[int]
    START_BOUND_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FRAME_UNITS_FIELD_NUMBER: _ClassVar[int]
    bound: WindowFrameBound
    start_bound: WindowFrameBound
    window_frame_units: WindowFrameUnits
    def __init__(
        self,
        window_frame_units: _Optional[_Union[WindowFrameUnits, str]] = ...,
        start_bound: _Optional[_Union[WindowFrameBound, _Mapping]] = ...,
        bound: _Optional[_Union[WindowFrameBound, _Mapping]] = ...,
    ) -> None: ...

class WindowFrameBound(_message.Message):
    __slots__ = ["bound_value", "window_frame_bound_type"]
    BOUND_VALUE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FRAME_BOUND_TYPE_FIELD_NUMBER: _ClassVar[int]
    bound_value: _arrow_pb2.ScalarValue
    window_frame_bound_type: WindowFrameBoundType
    def __init__(
        self,
        window_frame_bound_type: _Optional[_Union[WindowFrameBoundType, str]] = ...,
        bound_value: _Optional[_Union[_arrow_pb2.ScalarValue, _Mapping]] = ...,
    ) -> None: ...

class ScalarFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AggregateFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class BuiltInWindowFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class WindowFrameUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class WindowFrameBoundType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
