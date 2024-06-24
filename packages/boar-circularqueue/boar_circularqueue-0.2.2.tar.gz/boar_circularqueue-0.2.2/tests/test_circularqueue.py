#!/usr/bin/env python
import pytest

"""Tests for `circularqueue` package."""
from datetime import datetime
from boar_circularqueue.utility import get_logger
import unittest

from boar_circularqueue.container import CircularQueue
from boar_circularqueue.data import Node, INVALID_NODE_SEQ

logger = get_logger(__name__)


class TestCircularqueue(unittest.TestCase):
    """Tests for `circularqueue` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""


@pytest.fixture()
def get_test_payload():
    return {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4",
        "key5": "value5",
    }


@pytest.fixture()
def get_test_payload_inx():
    def _get(index: int):
        return {
            "sequence": index,
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
            "key4": "value4",
            "key5": "value5",
        }

    return _get


def test_data_marshal(get_test_payload) -> None:
    dummy_payload = get_test_payload
    node = Node(0, 0)
    now = datetime.now()
    node.replace_contents(sequence_number=1, input_date=now, payload=dummy_payload)

    assert node.get_payload() == dummy_payload
    assert isinstance(node.get_payload(), dict)
    assert node.sequence_number == 1
    assert node.get_datetime() == now
    pass


def test_circularqueue_init(get_test_payload):
    queue = CircularQueue(5)
    assert queue.size() == 5
    assert queue.length() == 0
    assert queue._container[0].sequence_number == INVALID_NODE_SEQ
    assert queue._container[1].sequence_number == INVALID_NODE_SEQ

    queue._container[0].replace_contents(
        sequence_number=1, input_date=datetime.now(), payload=get_test_payload
    )
    assert queue._container[0].get_payload() == get_test_payload
    assert queue._container[0].sequence_number == 1
    for i in range(1, 5):
        assert queue._container[i].sequence_number == INVALID_NODE_SEQ
        assert queue._container[i].payload == None


def test_circlarqueue_add_overflow(get_test_payload):
    queue = CircularQueue(5)
    size = queue.size()
    TOTAL_SIZE: int = 100
    for i in range(TOTAL_SIZE):
        queue.add(get_test_payload)
        assert queue.length() == min(i + 1, size)
        assert queue._container[i % size].sequence_number == i
        assert queue._container[i % size].get_payload() == get_test_payload
    pass


def test_circlarqueue_add_full_then_remove(get_test_payload_inx):
    queue = CircularQueue(5)
    size = queue.size()
    TOTAL_SIZE: int = 100
    for i in range(TOTAL_SIZE):
        queue.add(get_test_payload_inx(i))
        assert queue.length() == min(i + 1, size)
        assert queue._container[i % size].sequence_number == i
        assert queue._container[i % size].get_payload() == get_test_payload_inx(i)

    cnt = 0

    # Dequeue all items 95 to 99
    while not queue.is_empty():
        content = queue.remove()
        assert content == get_test_payload_inx(TOTAL_SIZE - size + cnt)
        cnt += 1

    cnt = TOTAL_SIZE
    queue.add(get_test_payload_inx(cnt))
    cnt += 1
    queue.add(get_test_payload_inx(cnt))
    cnt += 1

    content = queue.remove()
    assert content is not None
    assert content["sequence"] == TOTAL_SIZE

    for i in range(size):
        queue.add(get_test_payload_inx(cnt + i))

    assert queue.length() == size
    content = queue.remove()
    assert content is not None
    assert content["sequence"] == TOTAL_SIZE + 2
    assert queue._write_ptr == TOTAL_SIZE + 7
    assert queue._read_ptr == TOTAL_SIZE + 3

    # Dequeue all items 103 to 106
    cnt = 8
    assert queue.peak() == get_test_payload_inx(queue._write_ptr - 1)
    while not queue.is_empty():
        assert queue.peek() == get_test_payload_inx(TOTAL_SIZE - size + cnt)
        content = queue.remove()
        assert content == get_test_payload_inx(TOTAL_SIZE - size + cnt)
        cnt += 1
    assert queue._write_ptr == TOTAL_SIZE + 7
    assert queue._read_ptr == TOTAL_SIZE + 7

    logger.debug([i.sequence_number for i in queue._container])
    logger.debug(f"last content:{content['sequence']}")
    logger.debug(f"write ptr:{queue._write_ptr}")
    logger.debug(f"read ptr:{queue._read_ptr}")

    cnt = 7
    for i in range(size):
        assert queue._write_ptr == TOTAL_SIZE + cnt + i
        queue.add(get_test_payload_inx(TOTAL_SIZE + cnt + i))
    content = queue.remove()
    assert content["sequence"] == TOTAL_SIZE + cnt
    assert queue._read_ptr == TOTAL_SIZE + cnt + 1

    while not queue.is_empty():
        queue.remove()
    logger.debug([i.sequence_number for i in queue._container])
    logger.debug(f"last content:{content['sequence']}")
    logger.debug(f"write ptr:{queue._write_ptr}")
    logger.debug(f"read ptr:{queue._read_ptr}")

    cnt = 12
    for i in range(size + 1):
        assert queue._write_ptr == TOTAL_SIZE + cnt + i
        queue.add(get_test_payload_inx(TOTAL_SIZE + cnt + i))

    content = queue.remove()
    assert content["sequence"] == TOTAL_SIZE + cnt + 1
    logger.debug([i.sequence_number for i in queue._container])
    logger.debug(f"last content:{content['sequence']}")
    logger.debug(f"write ptr:{queue._write_ptr}")
    logger.debug(f"read ptr:{queue._read_ptr}")

    logger.critical(f"{queue._dump()}")
    queue.add(get_test_payload_inx(TOTAL_SIZE + 18))
    logger.critical(f"{queue._dump()}")
    logger.debug(f"peek: {queue.peek()}")
    queue.add(get_test_payload_inx(TOTAL_SIZE + 19))
    logger.critical(f"{queue._dump()}")
    logger.debug(f"peek: {queue.peek()}")
    queue.add(get_test_payload_inx(TOTAL_SIZE + 20))
    logger.critical(f"{queue._dump()}")
    logger.debug(f"peek: {queue.peek()}")
    # logger.debug(f"write ptr:{queue._write_ptr}")
    # logger.debug(f"read ptr:{queue._read_ptr}")
    # logger.debug(f"peek: {queue.peek()}")
    # logger.critical(f"{queue._dump()}")
    # logger.debug(f"read: {queue.remove()}")
    # logger.critical(f"{queue._dump()}")

    queue.reset()
    pass


def test_circularqueue_peek_empty():
    queue = CircularQueue(5)
    size = queue.size()
    assert len(queue.peak_n_recent_elements(2)) == 0


def test_circularqueue_peek_more_than_exist(get_test_payload_inx):
    queue = CircularQueue(5)
    # insert 2 elements
    for i in range(2):
        queue.add(get_test_payload_inx(i))

    elements: list = queue.peak_n_recent_elements(5)
    assert len(elements) == 2
    for i, e in enumerate(elements):
        assert i == e["sequence"]

    queue.add(get_test_payload_inx(2))
    elements: list = queue.peak_n_recent_elements(5)
    assert len(elements) == 3

    for i, e in enumerate(elements):
        assert i == e["sequence"]


def test_circularqueue_peek_100_get_20(get_test_payload_inx):
    queue = CircularQueue(5)
    NUM_ELEMENTS: int = 100
    max_size: int = queue.size()
    for i in range(NUM_ELEMENTS):
        queue.add(get_test_payload_inx(i))
    contents: list = queue.peak_n_recent_elements(20)
    assert len(contents) == max_size

    for i, e in enumerate(contents):
        assert e["sequence"] == NUM_ELEMENTS - max_size + i


def test_circularqueue_peek_100_get_2(get_test_payload_inx):
    queue = CircularQueue(5)
    NUM_ELEMENTS: int = 100
    max_size: int = 2
    for i in range(NUM_ELEMENTS):
        queue.add(get_test_payload_inx(i))
    contents: list = queue.peak_n_recent_elements(max_size)
    assert len(contents) == max_size

    for i, e in enumerate(contents):
        assert e["sequence"] == NUM_ELEMENTS - max_size + i
