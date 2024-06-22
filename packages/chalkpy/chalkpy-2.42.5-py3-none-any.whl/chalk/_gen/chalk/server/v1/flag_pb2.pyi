from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2

DESCRIPTOR: _descriptor.FileDescriptor
FLAG_SCOPE_ENVIRONMENT: FlagScope
FLAG_SCOPE_TEAM: FlagScope
FLAG_SCOPE_UNSPECIFIED: FlagScope

class FeatureFlagValue(_message.Message):
    __slots__ = ["flag", "value"]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    flag: str
    value: bool
    def __init__(self, flag: _Optional[str] = ..., value: bool = ...) -> None: ...

class GetFeatureFlagsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetFeatureFlagsResponse(_message.Message):
    __slots__ = ["flags"]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    flags: _containers.RepeatedCompositeFieldContainer[FeatureFlagValue]
    def __init__(self, flags: _Optional[_Iterable[_Union[FeatureFlagValue, _Mapping]]] = ...) -> None: ...

class SetFeatureFlagRequest(_message.Message):
    __slots__ = ["flag", "scope", "value"]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    flag: str
    scope: FlagScope
    value: bool
    def __init__(
        self, flag: _Optional[str] = ..., value: bool = ..., scope: _Optional[_Union[FlagScope, str]] = ...
    ) -> None: ...

class SetFeatureFlagResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FlagScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
