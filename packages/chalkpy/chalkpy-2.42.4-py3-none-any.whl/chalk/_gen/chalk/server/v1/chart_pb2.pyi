from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Chart(_message.Message):
    __slots__ = ["series", "title", "x_timestamp_ms"]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    X_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    series: _containers.RepeatedCompositeFieldContainer[Series]
    title: str
    x_timestamp_ms: _containers.RepeatedScalarFieldContainer[int]
    def __init__(
        self,
        title: _Optional[str] = ...,
        series: _Optional[_Iterable[_Union[Series, _Mapping]]] = ...,
        x_timestamp_ms: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class Series(_message.Message):
    __slots__ = ["label", "points", "units"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    label: str
    points: _containers.RepeatedScalarFieldContainer[float]
    units: str
    def __init__(
        self, points: _Optional[_Iterable[float]] = ..., label: _Optional[str] = ..., units: _Optional[str] = ...
    ) -> None: ...
