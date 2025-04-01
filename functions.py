import requests
import urls
import body

# Создание заказа самоката пользователем


def post_new_order():
    req = requests.post(urls.URL_SERVICE+urls.URL_ORDER, json=body.user_body)
    return req


# Получение трек-номера заказа пользоателя
def get_track():
    track = post_new_order().json()['track']
    return track

 # Получение состава заказа по трек-номеру


def get_zakaz():
    track_number = get_track()
    req = requests.get(
        urls.URL_SERVICE+urls.URL_ORDER_TRACK + str(track_number))
    return req
