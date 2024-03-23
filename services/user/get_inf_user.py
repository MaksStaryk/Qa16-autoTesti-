import requests
from services.base_services import BaseService


class GetUser(BaseService):

    def get_inf(self, name: str):
        self.response = requests.get(f'https://petstore.swagger.io/v2/user/{name}')
        self.response_json = self.response.json()

    def assert_email(self, email):
        assert self.response_json['email'] == email

    def assert_user_name(self, some_user_name):
        assert self.response_json['username'] == some_user_name

    def asser_password(self, password):
        assert self.response_json['password'] == password



