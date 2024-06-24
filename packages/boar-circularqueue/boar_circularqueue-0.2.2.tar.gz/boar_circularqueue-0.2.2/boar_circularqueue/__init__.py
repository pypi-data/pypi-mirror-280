"""Top-level package for CircularQueue."""

__author__ = """Dexter Chan"""
__email__ = 'dexterchan@example.com'
__version__ = '0.2.2'

from .container import CircularQueue

def create_instance(size:int) -> CircularQueue:
    return CircularQueue(size)