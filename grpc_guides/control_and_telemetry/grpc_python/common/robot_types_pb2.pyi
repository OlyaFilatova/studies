from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MotorDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTOR_DIRECTION_UNSPECIFIED: _ClassVar[MotorDirection]
    FORWARD: _ClassVar[MotorDirection]
    BACKWARD: _ClassVar[MotorDirection]
    STOP: _ClassVar[MotorDirection]
MOTOR_DIRECTION_UNSPECIFIED: MotorDirection
FORWARD: MotorDirection
BACKWARD: MotorDirection
STOP: MotorDirection

class MotorCommand(_message.Message):
    __slots__ = ("motor_id", "direction", "speed")
    MOTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    motor_id: int
    direction: MotorDirection
    speed: float
    def __init__(self, motor_id: _Optional[int] = ..., direction: _Optional[_Union[MotorDirection, str]] = ..., speed: _Optional[float] = ...) -> None: ...

class RobotState(_message.Message):
    __slots__ = ("emergency_stop", "battery_level")
    EMERGENCY_STOP_FIELD_NUMBER: _ClassVar[int]
    BATTERY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    emergency_stop: bool
    battery_level: float
    def __init__(self, emergency_stop: bool = ..., battery_level: _Optional[float] = ...) -> None: ...
