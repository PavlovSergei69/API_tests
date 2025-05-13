import httpx
from jsonschema import validate
from Core.contracts import LIST_RESOURCE_SCHEME

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
SINGLE_RESOURCE_NF = "api/unknown/23"

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()["data"]
    for item in data:
        validate(item, LIST_RESOURCE_SCHEME)

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_RESOURCE_SCHEME)

def test_single_resource_nf():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE_NF)
    assert response.status_code == 404