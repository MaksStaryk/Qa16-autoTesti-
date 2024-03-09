import requests
from services.base_services import BaseService



class CreateOrder(BaseService):

    def create_order(self, order):
        self.response = requests.post('https://petstore.swagger.io/v2/store/order', json= order)
        self.response_json = self.response.json()



