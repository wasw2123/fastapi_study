from temp import add, mul


def test_add() -> None:
    result = add(1, 2)
    assert result == 3


def test_mul() -> None:
    result = mul(2, 2)
    assert result == 4
