import pytest


@pytest.mark.grp1
def test_first():
    print("Hello")

@pytest.mark.xfail
def test_greet():
    print("Morning")
