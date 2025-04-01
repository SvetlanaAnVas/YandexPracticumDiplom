import functions
import body



# Тест на получение заказа по треку заказа, код ответа равен 200
def test_get_order_sucsess():
    req= functions.get_zakaz().status_code
    assert req==200
    