from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESS: _ClassVar[StatusCode]
    ALREADY_EXISTS: _ClassVar[StatusCode]
    NOT_FOUND: _ClassVar[StatusCode]
    INVALID_INFO: _ClassVar[StatusCode]
    PERMISSION_DENIED: _ClassVar[StatusCode]
    SERVER_ERROR: _ClassVar[StatusCode]
SUCCESS: StatusCode
ALREADY_EXISTS: StatusCode
NOT_FOUND: StatusCode
INVALID_INFO: StatusCode
PERMISSION_DENIED: StatusCode
SERVER_ERROR: StatusCode

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("id", "name", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class DeviceResponse(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: StatusCode
    message: str
    def __init__(self, code: _Optional[_Union[StatusCode, str]] = ..., message: _Optional[str] = ...) -> None: ...

class DeviceList(_message.Message):
    __slots__ = ("devices",)
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[DeviceInfo]
    def __init__(self, devices: _Optional[_Iterable[_Union[DeviceInfo, _Mapping]]] = ...) -> None: ...

class CommandRequest(_message.Message):
    __slots__ = ("device_id", "command", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    command: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, device_id: _Optional[str] = ..., command: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CommandResponse(_message.Message):
    __slots__ = ("device_id", "success", "message")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    success: bool
    message: str
    def __init__(self, device_id: _Optional[str] = ..., success: bool = ..., message: _Optional[str] = ...) -> None: ...

class SensorRequest(_message.Message):
    __slots__ = ("device_id", "metrics", "sample_interval_ms")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    metrics: _containers.RepeatedScalarFieldContainer[str]
    sample_interval_ms: int
    def __init__(self, device_id: _Optional[str] = ..., metrics: _Optional[_Iterable[str]] = ..., sample_interval_ms: _Optional[int] = ...) -> None: ...

class SensorData(_message.Message):
    __slots__ = ("device_id", "readings", "timestamp")
    class ReadingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    READINGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    readings: _containers.ScalarMap[str, float]
    timestamp: int
    def __init__(self, device_id: _Optional[str] = ..., readings: _Optional[_Mapping[str, float]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("device_id", "type", "message", "timestamp")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    type: str
    message: str
    timestamp: int
    def __init__(self, device_id: _Optional[str] = ..., type: _Optional[str] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
