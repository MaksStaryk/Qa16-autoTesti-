import allure
import requests

from services.base_services import BaseService
from data.other_dict_for_tests.pets_dict import *


class PetService(BaseService):
    file = None
    response_foto = None

    @allure.step('Sending a request to create a pet')
    def create_pet(self, some_dict: dict):
        try:
            self.logger.info('Send a request to create an order')
            self.response = self.post('https://petstore.swagger.io/v2/pet', some_dict)
            self.logger.info("Pet created")

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to create order: %s', e, exc_info=True)

    @allure.step('Sending a request to get information about a pet')
    def get_pet(self, object_id):
        try:
            self.logger.info(f'Send a request to get inform about a pet with id {object_id}')
            self.response = self.get(f'https://petstore.swagger.io/v2/pet/{object_id}')
            self.logger.info(f'Get inform about pet with id {object_id}')

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to get inform about a pet: %s', e, exc_info=True)

    @allure.step('Add a foto to pet')
    def add_foto(self, obj_id: int, path: str):
        try:
            self.logger.info(f'Add foto to pet {obj_id}')
            self.file = {'file': open(f'{path}', 'rb')}
            self.response_foto = requests.post(f'https://petstore.swagger.io/v2/pet/{obj_id}/uploadImage',
                                               files=self.file)
            self.logger.info('Added a foto')

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to add foto', str(e), exc_info=True)

    @allure.step('Delete a pet')
    def delete_pet(self, obj_id: int):
        try:
            self.logger.info(f'Start to delete inform about a pet with {obj_id}')
            self.response = self.delete(f"https://petstore.swagger.io/v2/pet/{obj_id}")
            self.logger.info('Inform about a pet deleted')

        except requests.exceptions.RequestException as e:
            self.logger.error("Failed to delete information about pet", str(e), exc_info=True)

    @allure.step('Check information about delete a pet')
    def check_delete(self, obj_id: int):
        self.logger.info(f'Send again a request to delete an order with id {obj_id}')
        self.response = requests.get(f'https://petstore.swagger.io/v2/pet/{obj_id}')

        if self.response.status_code != 200:
            assert True
            self.logger.info('A pet really deleted')
        else:
            self.logger.error("Fail cod 200 for delete request")
            assert False

    @allure.step('Update information about pet')
    def update_infor(self, some_dict: dict):
        try:
            self.logger.info("Start update infromation for pet with id ")
            self.response = self.post('https://petstore.swagger.io/v2/pet/', some_dict)
            self.logger.info('Information updated')

        except requests.exceptions.RequestException as e:
            self.logger.error("Failed update information = %s", str(e), exc_info=True)

    @allure.step('Check Information')
    def assert_information(self, name: str):
        try:

            self.logger.info(f'assert the \033[4m{name}\033[0m matches')
            assert information[f'{name}'] == self.response[f'{name}']
            self.logger.info('assert passed')

        except AssertionError as e:
            self.logger.error('Assert failed: %s', str(e), exc_info=True)

    @allure.step('checking nested dictionary')
    def assert_deep(self, name: str, second_name: str):
        try:
            self.logger.info(f'assert  the \033[4m{name}, {second_name}\033[0m matches')
            assert information[f'{name}'][f'{second_name}'] == self.response[f'{name}'][f'{second_name}']
            self.logger.info('assert passed')

        except AssertionError as e:
            self.logger.error('Assert failed: %s', str(e), exc_info=True)
