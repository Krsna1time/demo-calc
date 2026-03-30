from calculator import divide, add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    # This test FAILS with the current buggy code
    result = divide(10, 0)
    assert result == "Error: division by zero"


def test_divide_negative():
    assert divide(-6, 2) == -3.0
