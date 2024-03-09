import requests

from services.base_services import BaseService


class CreatePet(BaseService):
    file = None
    response_foto = None

    def add_pets(self, inform):
        self.response = requests.post("https://petstore.swagger.io/v2/pet", json=inform)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name

    def add_photo(self, obj_id, path):
        self.file = {'file': open(f'{path}', 'rb')}
        self.response_foto = requests.post(f'https://petstore.swagger.io/v2/pet/{obj_id}/uploadImage',
                                           files=self.file)

    def check_add_photo(self):
        assert self.response_foto.status_code == 200, 'in foto not 200 code'
