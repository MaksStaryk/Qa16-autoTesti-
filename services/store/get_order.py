import requests
from services.base_services import BaseService

class GetOrder(BaseService):

    def get_order(self, obj_id):
        self.response = requests.get(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
        self.response_json = self.response.json()

