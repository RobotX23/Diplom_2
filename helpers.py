import random
import string
import requests
from data import *

log3 = []


def new_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    name = generate_random_string(10)
    password = generate_random_string(10)
    first_name_email = generate_random_string(10) + '@yandex.ru'

    # собираем тело запроса
    payload = {
        "email": first_name_email,
        "password": password,
        "name": name
    }

    return payload


def old_user():
    returne = Old_user
    response = requests.post(f"{url}{register}", json=returne)
    return response.status_code

def old_user_1():
    returne = Old_user_1
    response = requests.post(f"{url}{register}", json=returne)
    return response.status_code