from hypothesis import given
from hypothesis import strategies as st

from source.heapsort import heapsort


@given(st.lists(st.integers()))
def test_heapsort_matches_sorted(xs):
    a = xs[:]
    heapsort(a)
    assert a == sorted(xs)
