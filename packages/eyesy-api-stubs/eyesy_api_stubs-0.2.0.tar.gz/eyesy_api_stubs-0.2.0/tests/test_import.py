from importlib.util import find_spec


def test_import():
    assert find_spec("eyesy_api_stubs")
