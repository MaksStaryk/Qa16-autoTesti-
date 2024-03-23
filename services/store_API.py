import allure
import requests
from services.base_services import BaseService
from data.other_dict_for_tests.order_dict import *


class StoreService(BaseService):
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

    @allure.step('Check information about delete a pet')
    def check_delete(self, obj_id):
        self.logger.info(f'Send again a request to delete an order with id {obj_id}')
        self.response = requests.get(f'https://petstore.swagger.io/v2/store/order/{obj_id}')

        if self.response.status_code != 200:

            assert True
            self.logger.info('Order really deleted')
        else:
            self.logger.error("Fail cod 200 for delete request")
            assert False

    @allure.step('Sending a request to get information about an order')
    def get_order(self, obj_id):
        try:
            self.logger.info(f'Send a request to get inform about an order with id {obj_id}')
            self.response = requests.get(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
            self.response_json = self.response.json()

            self.logger.info(f'Get inform about order with id {obj_id}')
            return self.response_json

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to get inform about an order: %s', e, exc_info=True)

    @allure.step(f'Check information')
    def assert_information(self, name: str):
        try:
            self.logger.info(f'assert the \033[4m{name}\033[0m matches')
            assert order_1[f'{name}'] == self.response_json[f'{name}']

            self.logger.info('Check passed')

        except AssertionError as e:
            self.logger.error('Check failed: %s', str(e), exc_info=True)
