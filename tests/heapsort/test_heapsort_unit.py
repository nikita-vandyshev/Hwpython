from source.heapsort import heapsort


def run_case(inp, expected):
    a = inp[:]
    heapsort(a)
    assert a == expected


def test_simple():
    run_case([3, 1, 2], [1, 2, 3])


def test_already_sorted():
    run_case([1, 2, 3, 4], [1, 2, 3, 4])


def test_reverse_sorted():
    run_case([4, 3, 2, 1], [1, 2, 3, 4])


def test_duplicates():
    run_case([2, 1, 2, 1], [1, 1, 2, 2])
