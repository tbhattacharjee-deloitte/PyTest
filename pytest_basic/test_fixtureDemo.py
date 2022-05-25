import pytest


@pytest.mark.usefixtures("setup")
class TestFixture:
    def test_fixture1(self):
        print("Fixture 1")

    def test_fixture2(self):
        print("Fixture 2")

    def test_fixture3(self):
        print("Fixture 3")
