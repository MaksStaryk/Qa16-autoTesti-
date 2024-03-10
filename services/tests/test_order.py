from services.store.create_order import CreateOrder
from services.other_dict_for_tests.order_dict import *
from services.store.delete_order import DeleteOrder
from services.store.get_order import GetOrder


def test_add_order():
    add_order = CreateOrder()
    add_order.create_order(order_1)
    add_order.check_cod_200()


def test_get_order():
    get_ord = GetOrder()
    get_ord.get_order(2)
    get_ord.check_cod_200()
    get_ord.check_id(2)


def test_delete_order():
    delete_order = DeleteOrder()
    delete_order.delete_order(2)
    delete_order.check_cod_200()
    delete_order = GetOrder()
    delete_order.get_order(2)
    delete_order.status_404()
