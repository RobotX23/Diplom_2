from helpers import *
import requests
from data import *

class TestUser:

    #Проверка создания пользователя
    def test_creating_user(self):
        returne = new_user()
        response = requests.post(f"{url}{register}", json=returne)
        assert response.status_code == 200 and response.json()["success"] is True

    #Проверка создания существующего пользователя
    def test_creating_user_old(self):
        returne = Old_user
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "User already exists" and response.json()["success"] is False

    #Проверка создания пользователя без имени
    def test_creating_user_no_name(self):
        returne = Old_user
        del returne["name"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False

    #Проверка создания пользователя без пароля
    def test_creating_user_no_password(self):
        returne = Old_user
        del returne["password"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False

    #Проверка создания пользователя без email
    def test_creating_user_no_email(self):
        returne = Old_user
        del returne["email"]
        response = requests.post(f"{url}{register}", json=returne)
        assert response.json()["message"] == "Email, password and name are required fields" and response.json()["success"] is False