import allure
from services.store_API import StoreService1
from services.other_dict_for_tests.order_dict import *


@allure.title("Path from creating, updating an order to deleting")
def test_order():
    order = StoreService1()
    order.create_order(order_1)
    order.get_order
    order.assert_information('status')
    order.assert_information('id')
    order.delete_order(2)
