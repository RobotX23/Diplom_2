from helpers import *
import requests
from data import *
import allure


class TestAuthorization:

    #Проверка авторизации
    @allure.title('Проверка авторизации')
    def test_authorization(self):
        returne = Old_user_avt
        old_user()
        response = requests.post(f"{url}{authorization}", json=returne)
        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["email"] == "tes1233335t-data@yandex.ru" and response.json()["user"]["name"] == "Lol134123"
        token_1 = {'Authorization': response.json()["accessToken"]}
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка авторизации с неверной почтой
    @allure.title('Проверка авторизации с неверной почтой')
    def test_authorization_no_email(self):
        return_1 = Old_user_avt
        returne = Old_user_avt_no_email
        old_user()
        response = requests.post(f"{url}{authorization}", json=returne)
        assert response.status_code == 401 and response.json()["success"] is False and response.json()["message"] == 'email or password are incorrect'
        b = requests.post(f"{url}{authorization}", json=return_1)
        token_1 = {'Authorization': b.json()["accessToken"]}
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка авторизации с неверным паролем
    @allure.title('Проверка авторизации с неверным паролем')
    def test_authorization_no_password(self):
        return_1 = Old_user_avt
        returne = Old_user_avt_no_password
        old_user()
        response = requests.post(f"{url}{authorization}", json=returne)
        assert response.status_code == 401 and response.json()["success"] is False and response.json()["message"] == 'email or password are incorrect'
        b = requests.post(f"{url}{authorization}", json=return_1)
        token_1 = {'Authorization': b.json()["accessToken"]}
        requests.delete(f"{url}{deleted}", headers=token_1)

