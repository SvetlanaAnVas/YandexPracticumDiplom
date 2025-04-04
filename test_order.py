import functions
import body
# Светлана Васильева, 28-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест на получение заказа по треку заказа, код ответа равен 200


def test_get_order_sucsess():
    create_order = functions.post_new_order(body.user_body)
    track = create_order.json()['track']
    get_zakaz_by_track = functions.get_zakaz(track)
    assert get_zakaz_by_track.status_code == 200
