import requests
from services.base_services import BaseService


class DeleteUser(BaseService):

    def delete_user(self, some_name: str):
        self.response = requests.delete(f'https://petstore.swagger.io/v2/user/{some_name}')
        self.response_json = self.response.json()
