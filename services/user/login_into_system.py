import requests
from services.base_services import BaseService


class Login(BaseService):

    def login_into(self, username: str, some_password):
        self.response = requests.get(
            f'https://petstore.swagger.io/v2/user/login?username={username}&password={some_password}')
        self.response_json = self.response.json()

    def check_login_into(self):
        assert 'logged in user session' in self.response_json['message'], 'we dont received message'

    def login_out(self):
        self.response = requests.get('https://petstore.swagger.io/v2/user/logout')
        self.response_json = self.response.json()