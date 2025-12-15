from hypothesis import given
from hypothesis import strategies as st

from source.bubble_sort import bubble_sort


@given(st.lists(st.integers()))
def test_bubble_sort_matches_sorted(xs):
    a = xs[:]
    bubble_sort(a)
    assert a == sorted(xs)
