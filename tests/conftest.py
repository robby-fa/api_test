# configuration for test
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://fakestoreapi.com/"

