from helpers import *
import requests
from data import *


class TestDateChange:

    #Проверка изменения email
    def test_email_avt(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        playgrop = {"email": New_user["email"]}
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        response_2 = requests.patch(f"{url}{deleted}", headers=token_1, data=playgrop)
        assert response_2.json()['success'] is True and response_2.json()['user']['email'] == New_user["email"] and response_2.json()['user']['name'] == Old_user_1["name"]
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка изменения пароля
    def test_passwor_avt(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        playgrop = {"password": New_user["password"]}
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        response_2 = requests.patch(f"{url}{deleted}", headers=token_1, data=playgrop)
        assert response_2.json()['success'] is True
        requests.delete(f"{url}{deleted}", headers=token_1)

    #Проверка изменения имени
    def test_name_avt(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        playgrop = {"name": New_user["name"]}
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        response_2 = requests.patch(f"{url}{deleted}", headers=token_1, data=playgrop)
        assert response_2.json()['success'] is True and response_2.json()['user']['email'] == Old_user_1["email"] and response_2.json()['user']['name'] == New_user["name"]
        requests.delete(f"{url}{deleted}", headers=token_1)


    #Проверка изменения у не авторизованного пользователя
    def test_no_avt(self):
        playgrop = {"name": New_user["name"]}
        response_2 = requests.patch(f"{url}{deleted}", data=playgrop)
        assert response_2.json()['message'] == 'You should be authorised'