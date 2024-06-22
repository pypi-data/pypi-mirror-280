from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.common.v1 import chalk_error_pb2 as _chalk_error_pb2
from chalk._gen.chalk.common.v1 import query_status_pb2 as _query_status_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DatasetFilter(_message.Message):
    __slots__ = ["max_cache_age_secs", "sample_filters"]
    MAX_CACHE_AGE_SECS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    max_cache_age_secs: float
    sample_filters: DatasetSampleFilter
    def __init__(
        self,
        sample_filters: _Optional[_Union[DatasetSampleFilter, _Mapping]] = ...,
        max_cache_age_secs: _Optional[float] = ...,
    ) -> None: ...

class DatasetResponse(_message.Message):
    __slots__ = ["dataset_id", "dataset_name", "environment_id", "errors", "is_finished", "revisions", "version"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    IS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    dataset_name: str
    environment_id: str
    errors: _containers.RepeatedCompositeFieldContainer[_chalk_error_pb2.ChalkError]
    is_finished: bool
    revisions: _containers.RepeatedCompositeFieldContainer[DatasetRevisionResponse]
    version: int
    def __init__(
        self,
        is_finished: bool = ...,
        version: _Optional[int] = ...,
        environment_id: _Optional[str] = ...,
        dataset_id: _Optional[str] = ...,
        dataset_name: _Optional[str] = ...,
        errors: _Optional[_Iterable[_Union[_chalk_error_pb2.ChalkError, _Mapping]]] = ...,
        revisions: _Optional[_Iterable[_Union[DatasetRevisionResponse, _Mapping]]] = ...,
    ) -> None: ...

class DatasetRevisionResponse(_message.Message):
    __slots__ = [
        "branch",
        "created_at",
        "creator_id",
        "dashboard_url",
        "dataset_id",
        "dataset_name",
        "environment_id",
        "filters",
        "givens_uri",
        "num_bytes",
        "num_partitions",
        "output_uris",
        "output_version",
        "outputs",
        "revision_id",
        "started_at",
        "status",
        "terminated_at",
    ]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_URL_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    GIVENS_URI_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URIS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VERSION_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TERMINATED_AT_FIELD_NUMBER: _ClassVar[int]
    branch: str
    created_at: _timestamp_pb2.Timestamp
    creator_id: str
    dashboard_url: str
    dataset_id: str
    dataset_name: str
    environment_id: str
    filters: DatasetFilter
    givens_uri: str
    num_bytes: int
    num_partitions: int
    output_uris: str
    output_version: int
    outputs: _containers.RepeatedScalarFieldContainer[str]
    revision_id: str
    started_at: _timestamp_pb2.Timestamp
    status: _query_status_pb2.QueryStatus
    terminated_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        dataset_name: _Optional[str] = ...,
        dataset_id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        revision_id: _Optional[str] = ...,
        creator_id: _Optional[str] = ...,
        outputs: _Optional[_Iterable[str]] = ...,
        givens_uri: _Optional[str] = ...,
        status: _Optional[_Union[_query_status_pb2.QueryStatus, str]] = ...,
        filters: _Optional[_Union[DatasetFilter, _Mapping]] = ...,
        num_partitions: _Optional[int] = ...,
        num_bytes: _Optional[int] = ...,
        output_uris: _Optional[str] = ...,
        output_version: _Optional[int] = ...,
        branch: _Optional[str] = ...,
        dashboard_url: _Optional[str] = ...,
        created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        terminated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class DatasetSampleFilter(_message.Message):
    __slots__ = ["lower_bound", "max_samples", "upper_bound"]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    MAX_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    lower_bound: _timestamp_pb2.Timestamp
    max_samples: int
    upper_bound: _timestamp_pb2.Timestamp
    def __init__(
        self,
        lower_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        upper_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        max_samples: _Optional[int] = ...,
    ) -> None: ...
