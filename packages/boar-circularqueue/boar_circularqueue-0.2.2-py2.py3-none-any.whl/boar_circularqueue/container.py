"""Main module."""

from .data import Node
from datetime import datetime
from typing import Any
from .utility import get_logger


logger = get_logger(__name__)


class CircularQueue:
    """if bounded = True
    add will return False when the buffer is full
    """

    def __init__(self, size: int, bounded: bool = False) -> None:
        self._max_size = size
        self._write_ptr = 0
        self._read_ptr = 0
        self._container: list[Node] = [None] * self._max_size
        self._init_container()
        self._readbuffer = [None] * self._max_size
        self.bounded = bounded
        pass

    def _init_container(self) -> None:

        for i in range(self._max_size):
            self._container[i] = Node.create_dummy()
        pass

    def add(self, content: Any) -> bool:
        """add element into queue

        Args:
            content (Any): any value type

        Returns:
            bool: true if add was successful; false if buffer uses up
        """
        if self.is_full():
            return False
        now = datetime.now()
        inx: int = self._write_ptr % self._max_size
        self._container[inx].replace_contents(self._write_ptr, now, content)
        self._write_ptr += 1
        return True

    def remove(self) -> Any:
        if self.is_empty():
            return None
        max_size: int = self._max_size
        new_read_ptr: int = self._get_read_inx_adj_overflow()
        content = self._container[new_read_ptr % max_size].get_payload()
        new_read_ptr += 1
        self._read_ptr = new_read_ptr
        return content

    def peek(self) -> Any:
        if self.is_empty():
            return None
        max_size: int = self._max_size
        peek_ptr: int = self._get_read_inx_adj_overflow()
        content = self._container[peek_ptr % max_size].get_payload()
        return content

    def peak(self) -> Any:
        if self.is_empty():
            return None
        max_size: int = self._max_size
        peek_ptr: int = self.get_last_write_ptr()
        content = self._container[peek_ptr % max_size].get_payload()
        return content

    def peak_n_recent_elements(self, n: int) -> list:
        max_size: int = self._max_size
        read_last_n_elements = min(n, self.length())
        last_element: int = self._write_ptr
        start_read_inx = last_element - read_last_n_elements
        return [
            self._container[i % max_size].get_payload()
            for i in range(start_read_inx, last_element)
        ]

    def _get_read_inx_adj_overflow(self) -> int:
        max_size: int = self._max_size
        return max(self._read_ptr, self._write_ptr - max_size)

    def length(self) -> int:
        return min(self._write_ptr - self._read_ptr, self._max_size)

    def is_full(self) -> bool:
        if not self.bounded:
            return False
        if self.length() == self._max_size:
            return True
        return False

    def size(self) -> int:
        return self._max_size

    def is_empty(self) -> bool:
        return self.length() == 0

    def reset(self) -> None:
        self._read_ptr = self._write_ptr = 0
        self._init_container()

    def get_last_write_ptr(self) -> int:
        return self._write_ptr - 1

    def get_last_read_ptr(self) -> int:
        return self._read_ptr - 1

    def _dump(self) -> list:
        return [s.sequence_number for s in self._container]
