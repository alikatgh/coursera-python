import add_sub
import pytest


def add(a, b):
    assert add_sub.add(5, 5) == 10


def sub(a, b):
    assert add_sub.sub(5, 5) == 0
