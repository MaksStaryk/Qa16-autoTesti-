import requests
from services.base_services import BaseService

class DeleteOrder(BaseService):

    def delete_order(self, obj_id):
        self.response = requests.delete(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
        self.response_json = self.response.json()


