

import requests
from services.base_services import BaseService


class CreateUser(BaseService):

    def create_user(self, some_dict: dict):
        try:
            self.logger.info('Creating user with data')
            self.response = requests.post('https://petstore.swagger.io/v2/user', json=some_dict)
            self.response.raise_for_status()
            self.response_json = self.response.json()
            self.logger.info('User created with response: %s', self.response_json)

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to create user: %s', e, exc_info=True)



