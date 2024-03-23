import requests

from services.base_services import BaseService


class UpdatePet(BaseService):

    def update_inf(self, inform):
        self.response = requests.put(f'https://petstore.swagger.io/v2/pet/', json=inform)
        self.response_json = self.response.json()

    def assert_information_name(self, inform: str):
        assert self.response_json['name'] == inform
