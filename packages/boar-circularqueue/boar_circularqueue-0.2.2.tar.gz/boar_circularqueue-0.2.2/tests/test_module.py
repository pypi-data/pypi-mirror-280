import boar_circularqueue
from boar_circularqueue import CircularQueue



def test_init() -> None:
    queue:CircularQueue = boar_circularqueue.create_instance(100)
    assert queue is not None
    assert queue.length() == 0