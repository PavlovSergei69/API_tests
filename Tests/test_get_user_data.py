#2_вариант
import httpx
from jsonschema import validate
from Core.contracts import USER_DATA_SHEME

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
USER_NOT_FOUND = "api/users/99"

EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"

def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS)
    #assert инструмент для проверки того, что возвращается. Два "==" необходимо для сравнения, одно "=" для присваивания данных переменной
    assert response.status_code == 200
    data = response.json()["data"]
    #цикл проверяет отдельно каждый элемент date последовательно со схемой USER_DATA_SCHEME
    for item in data:
        validate(item, USER_DATA_SHEME)      #Сначала проверяем "что проверяем", а потом "с каким контрактом" сравниваем
        #endswath = "оканчивается на"
        assert item["email"].endswith(EMAIL_ENDS)
        assert item["avatar"].endswith(str(item["id"]) + AVATAR_ENDS)

def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    date = response.json()["data"]
    assert date["email"].endswith(EMAIL_ENDS)
    assert date["avatar"].endswith(str(date["id"]) + AVATAR_ENDS)

def test_user_not_found():
    response = httpx.get(BASE_URL + USER_NOT_FOUND)
    assert response.status_code == 404
