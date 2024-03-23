import requests
from services.base_services import BaseService


class CreateOrder(BaseService):

    def create_order(self, order):
        try:
            self.logger.info("Create order")
            self.response = requests.post('https://petstore.swagger.io/v2/store/order', json= order)
            self.response_json = self.response.json()

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to create order: %s', str(e), exc_info=True)


