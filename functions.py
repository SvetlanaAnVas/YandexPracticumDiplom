import requests
import urls
import body

# Создание заказа самоката пользователем


def post_new_order(body):
    req = requests.post(urls.URL_SERVICE+urls.URL_ORDER, json=body)
    return req

 # Получение состава заказа по трек-номеру


def get_zakaz(track_number):
    req = requests.get(
        urls.URL_SERVICE+urls.URL_ORDER_TRACK + str(track_number))
    return req
