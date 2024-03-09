import requests
from services.base_services import BaseService

class CreateUser(BaseService):

    def create_user(self, some_dict: dict):
        self.response = requests.post('https://petstore.swagger.io/v2/user', json=some_dict)
        self.response_json = self.response.json()



