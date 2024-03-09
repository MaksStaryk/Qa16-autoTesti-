import requests
from services.base_services import BaseService


class UpdateUser(BaseService):

    def update_inf(self, some_name: str, some_dict: dict):
        self.response = requests.put(f'https://petstore.swagger.io/v2/user/{some_name}',
                                     json=some_dict)
        r = self.response_json = self.response.json()
        return r


