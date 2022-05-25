import pytest


@pytest.mark.grp1
@pytest.mark.skip
def test_assert():
    msg = "hello"
    assert msg == "HI", "Failed due to missmatch"


@pytest.mark.grp1
def test_math():
    assert 2 + 4 == 6, "Math error"
