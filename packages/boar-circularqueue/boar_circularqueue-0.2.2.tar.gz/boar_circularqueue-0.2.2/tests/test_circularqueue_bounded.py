import pytest

from datetime import datetime
from boar_circularqueue.utility import get_logger

from boar_circularqueue.container import CircularQueue
from boar_circularqueue.data import Node, INVALID_NODE_SEQ

logger = get_logger(__name__)
MAX_SIZE: int = 8


@pytest.fixture()
def create_bounded_circular_queue() -> CircularQueue:
    return CircularQueue(size=MAX_SIZE, bounded=True)


@pytest.fixture
def prepare_circular_queue_write_ptr_at_middle(
    create_bounded_circular_queue,
) -> CircularQueue:
    queue_bounded: CircularQueue = create_bounded_circular_queue

    for i in range(queue_bounded.size()):
        queue_bounded.add(i)

    for i in range(int(queue_bounded.size() >> 1)):
        assert queue_bounded.remove() == i
        assert queue_bounded.add(MAX_SIZE + i)
    assert queue_bounded.get_last_write_ptr() == MAX_SIZE + (MAX_SIZE >> 1) - 1
    assert queue_bounded.get_last_read_ptr() == (MAX_SIZE >> 1) - 1
    return queue_bounded


def test_circular_queue_overflow(create_bounded_circular_queue) -> None:
    queue_bounded: CircularQueue = create_bounded_circular_queue

    for i in range(queue_bounded.size()):
        assert queue_bounded.add(i)
    assert queue_bounded.add(100) == False
    pass


def test_circular_queue_overflow_then_remove_add_again_ok(
    create_bounded_circular_queue,
) -> None:
    queue_bounded: CircularQueue = create_bounded_circular_queue

    for i in range(queue_bounded.size()):
        assert queue_bounded.add(i)

    assert not queue_bounded.add(100)
    logger.debug(queue_bounded._dump())
    removed_value = queue_bounded.remove()
    logger.debug(removed_value)
    assert removed_value == 0

    assert queue_bounded.add(queue_bounded.size())

    pass


def test_circular_queue_overflow_work_at_middle(
    prepare_circular_queue_write_ptr_at_middle,
) -> None:
    queue_bounded = prepare_circular_queue_write_ptr_at_middle
    assert queue_bounded.size() == MAX_SIZE
    next_write_cnt = queue_bounded.get_last_write_ptr() + 1

    for i in range(queue_bounded.size() >> 1):
        queue_bounded.remove()

    assert queue_bounded.length() << 1 == queue_bounded.size()
    logger.debug(next_write_cnt)
    for i in range(queue_bounded.size() >> 1):
        value = next_write_cnt + i
        assert queue_bounded.add(value)
        assert value == queue_bounded.get_last_write_ptr()
    assert queue_bounded.length() == MAX_SIZE
    assert not queue_bounded.add(100)
