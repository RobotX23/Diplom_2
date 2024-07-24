from helpers import *
import requests
from data import *


class TestReceivingOrders:

    #Проверка получения заказов конкретного пользователя
    def test_receiving_avt(self):
        returne = Old_user_avt_1
        old_user_1()
        response = requests.post(f"{url}{authorization}", json=returne)
        lol = response.json()['accessToken']
        token_1 = {'Authorization': lol}
        requests.post(f"{url}{Orders}", headers=token_1, data=Ingredient)
        response_1 = requests.get(f"{url}{Orders}", headers=token_1)
        assert response_1.json()["success"] is True

    #Проверка получения заказов не авторизованного пользователя
    def test_receiving_no_avt(self):
        response_1 = requests.get(f"{url}{Orders}")
        print(response_1.json())
        assert response_1.json()["success"] is False and response_1.json()["message"] == 'You should be authorised'
