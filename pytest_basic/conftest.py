import pytest


@pytest.fixture(scope="class")
def setup(request):
    print("\nOn test start")
    # print(request.cls.__name__)
    yield
    print("On test end")


@pytest.fixture()
def dataLoad():
    print("Data Loading....")
    return ["abc", "def", "ghi"]


@pytest.fixture(params=[("Chrome", "hello", "world"), ("Firefox", "abc"), ("IE", "LLL")])
def cross_browser(request):
    return request.param