from helpers import *
import requests
from data import *
import allure

class TestUser:

    #Проверка создания пользователя
    @allure.title('Проверка создания пользователя')
    def test_creating_user(self):
        returne = new_user()
        response = requests.post(f"{url}{register}", json=returne)
        assert response.status_code == 200 and response.json()["success"] is True
        del returne["name"]
        b = requests.post(f"{url}{authorization}", json=returne)
        token_1 = {'Authorization': b.json()["accessToken"]}
        requests.delete(f"{url}{deleted}", headers=token_1)


    #Проверка создания существующего пользователя
    @allure.title('Проверка создания существующего пользователя')
    def test_creating_user_old(self):
        returne = Old_user
        returne_1 = Old_user_avt
        old_user()
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "User already exists" and response.json()["success"] is False and response.status_code == 403
        b = requests.post(f"{url}{authorization}", json=returne_1)
        token_1 = {'Authorization': b.json()["accessToken"]}
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка создания пользователя без имени
    @allure.title('Проверка создания пользователя без имени')
    def test_creating_user_no_name(self):
        returne = Old_user
        del returne["name"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False and response.status_code == 403


    #Проверка создания пользователя без пароля
    @allure.title('Проверка создания пользователя без пароля')
    def test_creating_user_no_password(self):
        returne = Old_user
        del returne["password"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False and response.status_code == 403

    #Проверка создания пользователя без email
    @allure.title('Проверка создания пользователя без email')
    def test_creating_user_no_email(self):
        returne = Old_user
        del returne["email"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False and response.status_code == 403

