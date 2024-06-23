from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BloomFilter(_message.Message):
    __slots__ = ["data", "environment", "namespace", "num_entries", "num_expected_entries", "num_hashes", "size_bytes"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NUM_EXPECTED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NUM_HASHES_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    environment: str
    namespace: str
    num_entries: int
    num_expected_entries: int
    num_hashes: int
    size_bytes: int
    def __init__(
        self,
        environment: _Optional[str] = ...,
        namespace: _Optional[str] = ...,
        num_entries: _Optional[int] = ...,
        num_expected_entries: _Optional[int] = ...,
        num_hashes: _Optional[int] = ...,
        size_bytes: _Optional[int] = ...,
        data: _Optional[bytes] = ...,
    ) -> None: ...
