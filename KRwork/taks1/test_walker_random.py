import random

import pytest
from walker_random import WalkerRandom


def run_case(events, allowed):
    chooser = WalkerRandom(events)
    x = chooser.get_random()
    assert x in allowed


def test_simple():
    run_case(
        [("A", 0.5), ("B", 0.3), ("C", 0.2)],
        ["A", "B", "C"],
    )


def test_single_event():
    run_case(
        [("ONLY", 1.0)],
        ["ONLY"],
    )


def test_empty_events():
    with pytest.raises(ValueError):
        WalkerRandom([])


def test_bad_probability():
    with pytest.raises(ValueError):
        WalkerRandom([("A", 0.5), ("B", 0.0)])


def test_sum_not_one():
    with pytest.raises(ValueError):
        WalkerRandom([("A", 0.6), ("B", 0.3)])


def test_repeatable_with_seed():
    chooser = WalkerRandom([("A", 0.5), ("B", 0.3), ("C", 0.2)])

    random.seed(0)
    a = chooser.get_random()

    random.seed(0)
    b = chooser.get_random()

    assert a == b
