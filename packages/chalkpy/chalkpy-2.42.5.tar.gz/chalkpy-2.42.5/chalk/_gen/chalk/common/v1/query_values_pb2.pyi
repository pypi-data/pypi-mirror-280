from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.common.v1 import query_log_pb2 as _query_log_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueryValuesPageToken(_message.Message):
    __slots__ = ["operation_id_hwm", "query_timestamp_hwm", "row_id_hwm"]
    OPERATION_ID_HWM_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMESTAMP_HWM_FIELD_NUMBER: _ClassVar[int]
    ROW_ID_HWM_FIELD_NUMBER: _ClassVar[int]
    operation_id_hwm: str
    query_timestamp_hwm: _timestamp_pb2.Timestamp
    row_id_hwm: int
    def __init__(
        self,
        query_timestamp_hwm: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        operation_id_hwm: _Optional[str] = ...,
        row_id_hwm: _Optional[int] = ...,
    ) -> None: ...

class GetQueryValuesRequest(_message.Message):
    __slots__ = [
        "features",
        "operation_id_identifier",
        "page_size",
        "page_token",
        "query_timestamp_lower_bound_inclusive",
        "query_timestamp_upper_bound_exclusive",
        "table_name_identifier",
    ]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMESTAMP_LOWER_BOUND_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMESTAMP_UPPER_BOUND_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedScalarFieldContainer[str]
    operation_id_identifier: OperationIdTableIdentifier
    page_size: int
    page_token: str
    query_timestamp_lower_bound_inclusive: _timestamp_pb2.Timestamp
    query_timestamp_upper_bound_exclusive: _timestamp_pb2.Timestamp
    table_name_identifier: TableNameTableIdentifier
    def __init__(
        self,
        operation_id_identifier: _Optional[_Union[OperationIdTableIdentifier, _Mapping]] = ...,
        table_name_identifier: _Optional[_Union[TableNameTableIdentifier, _Mapping]] = ...,
        query_timestamp_lower_bound_inclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        query_timestamp_upper_bound_exclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        features: _Optional[_Iterable[str]] = ...,
        page_size: _Optional[int] = ...,
        page_token: _Optional[str] = ...,
    ) -> None: ...

class GetQueryValuesResponse(_message.Message):
    __slots__ = ["next_page_token", "parquet"]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARQUET_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    parquet: bytes
    def __init__(self, next_page_token: _Optional[str] = ..., parquet: _Optional[bytes] = ...) -> None: ...

class OperationIdTableIdentifier(_message.Message):
    __slots__ = ["operation_id"]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class TableNameTableIdentifier(_message.Message):
    __slots__ = ["filters", "table_name"]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    filters: _query_log_pb2.QueryLogFilters
    table_name: str
    def __init__(
        self,
        table_name: _Optional[str] = ...,
        filters: _Optional[_Union[_query_log_pb2.QueryLogFilters, _Mapping]] = ...,
    ) -> None: ...
