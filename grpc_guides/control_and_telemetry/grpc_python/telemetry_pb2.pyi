from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TelemetrySubscription(_message.Message):
    __slots__ = ("sensor_ids",)
    SENSOR_IDS_FIELD_NUMBER: _ClassVar[int]
    sensor_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sensor_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TelemetryMessage(_message.Message):
    __slots__ = ("sensor_id", "value", "timestamp_unix_ms")
    SENSOR_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    sensor_id: str
    value: float
    timestamp_unix_ms: int
    def __init__(self, sensor_id: _Optional[str] = ..., value: _Optional[float] = ..., timestamp_unix_ms: _Optional[int] = ...) -> None: ...
