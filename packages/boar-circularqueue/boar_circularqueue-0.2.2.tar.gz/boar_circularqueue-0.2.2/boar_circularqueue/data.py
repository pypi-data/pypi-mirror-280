from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass, field
from typing import Any, Optional
import pickle
import sys
from .utility import get_logger

PAYLOAD_SIZE: int = 256 * 1024

logger = get_logger(__name__)

INVALID_NODE_SEQ:int = -1
@dataclass
class Node:
    sequence_number: int
    timestamp: float
    payload: Optional[bytes] = None

    def __post_init__(self):
        if self.payload and (sys.getsizeof(self.payload)) > PAYLOAD_SIZE:
            raise ValueError(f"Payload size must be smaller than {PAYLOAD_SIZE} bytes")

    def __repr__(self):
        return f"Node({self.sequence_number}, {self.timestamp}, {self.payload})"

    def replace_contents(self, sequence_number:int, input_date:datetime, payload: Any):
        self.sequence_number = sequence_number
        self.timestamp = input_date.timestamp()
        if not isinstance(payload, bytes):
            payload = Node_Marshaller.serialize_object(payload)
        self.payload = payload
        self.__post_init__()

    def get_payload(self) -> Any:
        if self.payload:
            return Node_Marshaller.deserialize_object(self.payload)
        return None
    
    def get_datetime(self)->datetime:
        return datetime.fromtimestamp(self.timestamp)
    
    def reset(self)->None:
        self.sequence_number = INVALID_NODE_SEQ
        self.timestamp = 0
        self.payload = None
    
    def is_valid(self)->bool:
        return self.sequence_number != INVALID_NODE_SEQ

    @classmethod
    def create_dummy(cls)->Node:
        return Node(sequence_number=INVALID_NODE_SEQ, timestamp=0)


class Node_Marshaller:
    def serialize_object(object: Any) -> bytes:
        return pickle.dumps(object)

    def deserialize_object(rawdata: bytes) -> Any:
        return pickle.loads(rawdata)
