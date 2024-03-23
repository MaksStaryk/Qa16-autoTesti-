import requests
from services.base_services import BaseService


class DeleteOrder(BaseService):

    def delete_order(self, obj_id):
        try:
            self.logger.info(f'Delete user with {obj_id}')
            self.response = requests.delete(f'https://petstore.swagger.io/v2/store/order/{obj_id}')
            self.response.raise_for_status()
            self.response_json = self.response.json()
            self.logger.info('Information was deleted')

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to delete user: %s', str(e), exc_info=True)
