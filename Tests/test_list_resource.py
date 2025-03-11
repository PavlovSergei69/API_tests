import httpx
from jsonschema import validate
from Core.contracts import LIST_RESOURCE_SCHEME

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
SINGLE_RESOURCE_NF = 'api/unknown/23'

def test_list_resource():
    responce = httpx.get(BASE_URL + LIST_RESOURCE)
    assert responce.status_code == 200
    data = responce.json()['data']
    for item in data:
        validate(item, LIST_RESOURCE_SCHEME)

def test_single_resource():
    responce = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert responce.status_code == 200
    data = responce.json()['data']
    validate(data, LIST_RESOURCE_SCHEME)

def test_single_resource_nf():
    responce = httpx.get(BASE_URL + SINGLE_RESOURCE_NF)
    assert responce.status_code == 404