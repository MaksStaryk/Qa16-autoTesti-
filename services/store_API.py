import allure
import requests
from services.base_services import BaseService
from  services.other_dict_for_tests.order_dict import *


class StoreService1(BaseService):
    @allure.step('Sending a request to create an order')
    def create_order(self, some_order: dict):
        try:
            self.logger.info('Send a request to create an order')
            self.response = self.post('https://petstore.swagger.io/v2/store/order', some_order)
            self.logger.info("Order created")

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to create order: %s', e, exc_info=True)

    @allure.step('Sending a request to delete an order')
    def delete_order(self, obj_id):
        try:
            self.logger.info(f'Send a request to delete an order with id {obj_id}')
            self.response = self.delete(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
            self.logger.info("Order deleted")

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to delete order: %s', e, exc_info=True)

    @allure.step('Sending a request to get information about an order')
    def get_order(self, obj_id):
        try:
            self.logger.info(f'Send a request to get inform about an order with id {obj_id}')
            self.response = requests.get(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
            self.logger.info(f'Get inform about order with id {obj_id}')

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to get inform about an order: %s', e, exc_info=True)

    @allure.step('Check information')
    def assert_information(self, name: str):
        try:
            self.logger.info(f'assert the \033[4m{name}\033[0m matches')
            assert order_1[f'{name}'] == self.response[f'{name}']
            self.logger.info('Check passed')

        except requests.exceptions.RequestException as e:
            self.logger.error('Check failed', str(e), exc_info=True)
