from helpers import *
import requests
from data import *
import allure


class TestCreateAnOrder:

    #Проверка создание заказа авторизованным пользователем
    @allure.title('Проверка создание заказа авторизованным пользователем')
    def test_avt(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        r = requests.post(f"{url}{Orders}", headers=token_1, data=Ingredient)
        assert r.json()["success"] is True and r.status_code == 200
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка создание заказа не авторизованным пользователем
    #Не корректная обработка сервером
    @allure.title('Проверка создание заказа не авторизованным пользователем')
    @allure.description("Не корректная обработка сервером, должен быть код 401, а возвращает 200")
    def test_no_avt(self):
        r = requests.post(f"{url}{Orders}",  data=Ingredient)
        assert r.json()["success"] is True and r.status_code == 200


    #Проверка создание заказа авторизованным пользователем без ингридиентов
    @allure.title('Проверка создание заказа авторизованным пользователем без ингридиентов')
    def test_avt_no_ing(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        r = requests.post(f"{url}{Orders}", headers=token_1)
        assert r.json()["success"] is False and r.json()["message"] == 'Ingredient ids must be provided' and r.status_code == 400
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка создание заказа авторизованным пользователем с неверным хешем ингредиентов
    @allure.title('Проверка создание заказа авторизованным пользователем с неверным хешем ингредиентов')
    def test_no_hesh(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        r = requests.post(f"{url}{Orders}", headers=token_1, data=No_hesh_ngredient)
        assert r.status_code == 500
        requests.delete(f"{url}{deleted}", headers=token_1)

