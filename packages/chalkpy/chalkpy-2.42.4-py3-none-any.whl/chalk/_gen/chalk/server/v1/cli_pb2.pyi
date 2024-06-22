from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CommandLineInterfaceVersion(_message.Message):
    __slots__ = ["arch", "download_url", "generation", "os", "version"]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    arch: str
    download_url: str
    generation: int
    os: str
    version: str
    def __init__(
        self,
        version: _Optional[str] = ...,
        download_url: _Optional[str] = ...,
        os: _Optional[str] = ...,
        arch: _Optional[str] = ...,
        generation: _Optional[int] = ...,
    ) -> None: ...

class GetVersionsRequest(_message.Message):
    __slots__ = ["arch", "os"]
    ARCH_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    arch: str
    os: str
    def __init__(self, os: _Optional[str] = ..., arch: _Optional[str] = ...) -> None: ...

class GetVersionsResponse(_message.Message):
    __slots__ = ["latest", "minimum", "nightly", "versions"]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    NIGHTLY_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    latest: CommandLineInterfaceVersion
    minimum: str
    nightly: CommandLineInterfaceVersion
    versions: _containers.RepeatedCompositeFieldContainer[CommandLineInterfaceVersion]
    def __init__(
        self,
        versions: _Optional[_Iterable[_Union[CommandLineInterfaceVersion, _Mapping]]] = ...,
        latest: _Optional[_Union[CommandLineInterfaceVersion, _Mapping]] = ...,
        nightly: _Optional[_Union[CommandLineInterfaceVersion, _Mapping]] = ...,
        minimum: _Optional[str] = ...,
    ) -> None: ...
