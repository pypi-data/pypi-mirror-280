from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor
DIAGNOSTIC_SEVERITY_ERROR: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_HINT: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_INFORMATION: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_UNSPECIFIED: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_WARNING: DiagnosticSeverity

class CodeAction(_message.Message):
    __slots__ = ["diagnostics", "edit", "title"]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    EDIT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    edit: WorkspaceEdit
    title: str
    def __init__(
        self,
        title: _Optional[str] = ...,
        diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...,
        edit: _Optional[_Union[WorkspaceEdit, _Mapping]] = ...,
    ) -> None: ...

class CodeDescription(_message.Message):
    __slots__ = ["href"]
    HREF_FIELD_NUMBER: _ClassVar[int]
    href: str
    def __init__(self, href: _Optional[str] = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ["code", "code_description", "message", "range", "related_information", "severity"]
    CODE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    RELATED_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    code: str
    code_description: CodeDescription
    message: str
    range: Range
    related_information: _containers.RepeatedCompositeFieldContainer[DiagnosticRelatedInformation]
    severity: DiagnosticSeverity
    def __init__(
        self,
        range: _Optional[_Union[Range, _Mapping]] = ...,
        message: _Optional[str] = ...,
        severity: _Optional[_Union[DiagnosticSeverity, str]] = ...,
        code: _Optional[str] = ...,
        code_description: _Optional[_Union[CodeDescription, _Mapping]] = ...,
        related_information: _Optional[_Iterable[_Union[DiagnosticRelatedInformation, _Mapping]]] = ...,
    ) -> None: ...

class DiagnosticRelatedInformation(_message.Message):
    __slots__ = ["location", "message"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    location: Location
    message: str
    def __init__(
        self, location: _Optional[_Union[Location, _Mapping]] = ..., message: _Optional[str] = ...
    ) -> None: ...

class LSP(_message.Message):
    __slots__ = ["actions", "diagnostics"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[CodeAction]
    diagnostics: _containers.RepeatedCompositeFieldContainer[PublishDiagnosticsParams]
    def __init__(
        self,
        diagnostics: _Optional[_Iterable[_Union[PublishDiagnosticsParams, _Mapping]]] = ...,
        actions: _Optional[_Iterable[_Union[CodeAction, _Mapping]]] = ...,
    ) -> None: ...

class Location(_message.Message):
    __slots__ = ["range", "uri"]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    range: Range
    uri: str
    def __init__(self, uri: _Optional[str] = ..., range: _Optional[_Union[Range, _Mapping]] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ["character", "line"]
    CHARACTER_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    character: int
    line: int
    def __init__(self, line: _Optional[int] = ..., character: _Optional[int] = ...) -> None: ...

class PublishDiagnosticsParams(_message.Message):
    __slots__ = ["diagnostics", "uri"]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    uri: str
    def __init__(
        self, uri: _Optional[str] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...
    ) -> None: ...

class Range(_message.Message):
    __slots__ = ["end", "start"]
    END_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    end: Position
    start: Position
    def __init__(
        self, start: _Optional[_Union[Position, _Mapping]] = ..., end: _Optional[_Union[Position, _Mapping]] = ...
    ) -> None: ...

class TextDocumentEdit(_message.Message):
    __slots__ = ["edits", "text_document"]
    EDITS_FIELD_NUMBER: _ClassVar[int]
    TEXT_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    edits: _containers.RepeatedCompositeFieldContainer[TextEdit]
    text_document: TextDocumentIdentifier
    def __init__(
        self,
        text_document: _Optional[_Union[TextDocumentIdentifier, _Mapping]] = ...,
        edits: _Optional[_Iterable[_Union[TextEdit, _Mapping]]] = ...,
    ) -> None: ...

class TextDocumentIdentifier(_message.Message):
    __slots__ = ["uri"]
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class TextEdit(_message.Message):
    __slots__ = ["new_text", "range"]
    NEW_TEXT_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    new_text: str
    range: Range
    def __init__(self, range: _Optional[_Union[Range, _Mapping]] = ..., new_text: _Optional[str] = ...) -> None: ...

class WorkspaceEdit(_message.Message):
    __slots__ = ["document_changes"]
    DOCUMENT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    document_changes: _containers.RepeatedCompositeFieldContainer[TextDocumentEdit]
    def __init__(self, document_changes: _Optional[_Iterable[_Union[TextDocumentEdit, _Mapping]]] = ...) -> None: ...

class DiagnosticSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
