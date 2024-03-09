import requests

from services.base_services import BaseService


class DeletePet(BaseService):

    def delete_pet(self, obj_id: int):
        self.response = requests.delete(f"https://petstore.swagger.io/v2/pet/{obj_id}")
        self.response_json = self.response.json()



