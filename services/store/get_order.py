import requests
from services.base_services import BaseService


class GetOrder(BaseService):

    def get_order(self, obj_id):
        try:
            self.logger.info('Get information by id: %s', obj_id)
            self.response = requests.get(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
            self.response.raise_for_status()
            self.response_json = self.response.json()
            self.logger.info('Received information ')

        except requests.RequestException as e:
            self.logger.error('Failed to get user: %s', e, exc_info=True)
