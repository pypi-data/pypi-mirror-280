from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class CronQuery(_message.Message):
    __slots__ = [
        "cron",
        "file_name",
        "incremental_sources",
        "lower_bound",
        "max_samples",
        "name",
        "output",
        "recompute",
        "required_resolver_tags",
        "store_offline",
        "store_online",
        "tags",
        "upper_bound",
    ]
    CRON_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_SOURCES_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RECOMPUTE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_RESOLVER_TAGS_FIELD_NUMBER: _ClassVar[int]
    STORE_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    STORE_ONLINE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    cron: str
    file_name: str
    incremental_sources: _containers.RepeatedScalarFieldContainer[str]
    lower_bound: _timestamp_pb2.Timestamp
    max_samples: int
    name: str
    output: _containers.RepeatedScalarFieldContainer[str]
    recompute: RecomputeSettings
    required_resolver_tags: _containers.RepeatedScalarFieldContainer[str]
    store_offline: bool
    store_online: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    upper_bound: _timestamp_pb2.Timestamp
    def __init__(
        self,
        name: _Optional[str] = ...,
        cron: _Optional[str] = ...,
        file_name: _Optional[str] = ...,
        output: _Optional[_Iterable[str]] = ...,
        max_samples: _Optional[int] = ...,
        recompute: _Optional[_Union[RecomputeSettings, _Mapping]] = ...,
        lower_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        upper_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        required_resolver_tags: _Optional[_Iterable[str]] = ...,
        store_online: bool = ...,
        store_offline: bool = ...,
        incremental_sources: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class RecomputeSettings(_message.Message):
    __slots__ = ["all_features", "feature_fqns"]
    ALL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FQNS_FIELD_NUMBER: _ClassVar[int]
    all_features: bool
    feature_fqns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, feature_fqns: _Optional[_Iterable[str]] = ..., all_features: bool = ...) -> None: ...
