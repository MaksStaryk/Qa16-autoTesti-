import allure
from services.store_API import StoreService
from data.other_dict_for_tests.order_dict import *


@allure.title("Path from creating, updating an order to deleting")
def test_order():
    order = StoreService()
    order.create_order(order_1)
    order.get_order(2)
    order.assert_information('id')
    order.assert_information('status')
    order.delete_order(2)
    order.check_delete(2)
