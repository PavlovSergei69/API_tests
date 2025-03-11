#2_вариант
import httpx
from jsonschema import validate
from Core.contracts import USER_DATA_SHEME

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
SINGLE_USER = 'api/users/2'
USER_NOT_FOUND = 'api/users/23'

EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'

def test_list_users():
    responce = httpx.get(BASE_URL + LIST_USERS)
    #assert инструмент для проверки того, что возвращается. Два "==" необходимо для сравнения, одно "=" для присваивания данных переменной
    assert responce.status_code == 200
    data = responce.json()['data']
    #цикл проверяет отдельно каждый элемент date последовательно
    for item in data:
        validate(item, USER_DATA_SHEME)      #Сначала проверяем "что проверяем", а потом "с каким контрактом" сравниваем
        #endswath = "оканчивается на"
        assert item['email'].endswith(EMAIL_ENDS)
        assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

def test_single_users():
    responce = httpx.get(BASE_URL + SINGLE_USER)
    assert responce.status_code == 200
    date = responce.json()['data']
    assert date['email'].endswith(EMAIL_ENDS)
    assert date['avatar'].endswith(str(date['id']) + AVATAR_ENDS)

def test_user_not_found():
    responce = httpx.get(BASE_URL + USER_NOT_FOUND)
    assert responce.status_code == 404
