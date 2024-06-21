"""MyrtIO data protocol implementation"""

from .bytes import from_byte_pair, split_byte_pair
from .constants import (
    ERROR_CODE,
    FIRST_HEADER_CODE,
    MAX_MESSAGE_LENGTH,
    MIN_MESSAGE_LENGTH,
    SECOND_HEADER_CODE,
    SUCCESS_CODE,
    TAIL_CODE,
)
from .message import Message, parse_message
from .transport import MyrtIOTransport
