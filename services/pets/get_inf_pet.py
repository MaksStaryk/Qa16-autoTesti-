import requests
from my_logging import *
from services.base_services import BaseService


class GetPet(BaseService):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    def get_pet(self, object_id):

        self.response = requests.get(f'https://petstore.swagger.io/v2/pet/{object_id}')
        self.response_json = self.response.json()

    def get_inf(self, inform: str):
        print(self.response_json[f'{inform}'])

    def assert_name(self, name: str):
        assert self.response_json.get('category').get('name') == name, 'incorrect name'


