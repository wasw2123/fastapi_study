from temp import add


def test_add() -> None:
    result = add(1, 2)
    assert result == 3
