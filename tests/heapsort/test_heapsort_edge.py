from source.heapsort import heapsort


def test_empty():
    a = []
    heapsort(a)
    assert a == []


def test_one_element():
    a = [5]
    heapsort(a)
    assert a == [5]


def test_all_equal():
    a = [7, 7, 7]
    heapsort(a)
    assert a == [7, 7, 7]


def test_negative_numbers():
    a = [0, -1, -5, 2]
    heapsort(a)
    assert a == [-5, -1, 0, 2]