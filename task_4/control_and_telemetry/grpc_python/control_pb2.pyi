from common import robot_types_pb2 as _robot_types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMotorRequest(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: _robot_types_pb2.MotorCommand
    def __init__(self, command: _Optional[_Union[_robot_types_pb2.MotorCommand, _Mapping]] = ...) -> None: ...

class SetMotorResponse(_message.Message):
    __slots__ = ("accepted",)
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    def __init__(self, accepted: bool = ...) -> None: ...

class StopAllRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopAllResponse(_message.Message):
    __slots__ = ("stopped",)
    STOPPED_FIELD_NUMBER: _ClassVar[int]
    stopped: bool
    def __init__(self, stopped: bool = ...) -> None: ...

class LiveControlRequest(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: _robot_types_pb2.MotorCommand
    def __init__(self, command: _Optional[_Union[_robot_types_pb2.MotorCommand, _Mapping]] = ...) -> None: ...

class LiveControlResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _robot_types_pb2.RobotState
    def __init__(self, state: _Optional[_Union[_robot_types_pb2.RobotState, _Mapping]] = ...) -> None: ...
