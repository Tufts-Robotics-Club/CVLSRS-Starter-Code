from enum import Enum
from .target_pb2 import Target
from .rotationCommand_pb2 import RotationCommand
from .tiltCommand_pb2 import TiltCommand
from .text_pb2 import Text

class MsgType(Enum):
    TARGET = 0
    TILT_COMMAND = 1
    ROTATION_COMMAND = 2
    TEXT = 3

message_buffers = {
    MsgType.TARGET: Target,
    MsgType.TILT_COMMAND: TiltCommand,
    MsgType.ROTATION_COMMAND: RotationCommand,
    MsgType.TEXT: Text
}


__all__ = ['MsgType', 'message_buffers', 'Target', 'TiltCommand', 'RotationCommand', 'Text']