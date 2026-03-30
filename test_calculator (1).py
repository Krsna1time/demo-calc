from calculator import divide, add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        pass


def test_divide_negative():
    assert divide(-6, 2) == -3.0
