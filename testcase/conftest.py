import pytest
from conftest import get_departments_data

@pytest.fixture(params=get_departments_data["get_departments_id"])
def get_data(request):
    return request.param