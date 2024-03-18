import requests
from services.base_services import BaseService


class UserService1(BaseService):

    def create_user(self, some_dict: dict):
        try:
            self.logger.info('Creating user with data')
            self.response = self.post('https://petstore.swagger.io/v2/user', some_dict)
            self.logger.info('User created with response: %s')

        except requests.exceptions.RequestException as e:
            self.logger.error('Failed to create user1: %s', e, exc_info=True)

    def get_information(self, name: str):
        try:
            self.logger.info(f'Get information by {name}')
            self.response = self.get(f'https://petstore.swagger.io/v2/user/{name}')
            self.logger.info('Received information ')
            return self.response

        except requests.exceptions.RequestException as e:
            self.logger.info("User data  is not received", e, exc_info=True)

    def delete_user(self, some_name: str):
        try:
            self.logger.info(f"Try delete information for {some_name}")
            self.response = self.delete(f'https://petstore.swagger.io/v2/user/{some_name}')

        except requests.exceptions.RequestException as e:
            self.logger.info("user data is not deleted", e, exc_info=True)

    def check_delete(self, name: str):
        self.logger.info(f'try receive information by {name}')
        self.response = requests.get(f'https://petstore.swagger.io/v2/user/{name}')
        self.logger.info(f'information delete for {name}')

        if self.response.status_code != 200:
            assert True
        else:
            self.logger.info("Fail cod 200 for delete request")
            assert False

    def login_into(self, username: str, some_password):
        try:
            self.logger.info("login attempt")
            self.response = self.get(
                f'https://petstore.swagger.io/v2/user/login?username={username}&password={some_password}')

        except requests.exceptions.RequestException as e:
            self.logger.info("login attempt failed", e, exc_info=True)

    def update_information(self, some_name: str, some_dict: dict):
        try:
            self.logger.info(f"Try update information for {some_name}")
            self.response = self.put(f'https://petstore.swagger.io/v2/user/{some_name}',
                                     some_dict)

        except requests.exceptions.RequestException as e:
            self.logger.info("information update failed", str(e), exc_info=True)

    def enter_system(self, username: str, some_password):
        try:
            self.logger.info(f"user login for name {username}")
            self.response = self.get(
            f'https://petstore.swagger.io/v2/user/login?username={username}&password={some_password}')
            self.logger.info(f"{username} is logged in")

        except requests.exceptions.RequestException as e:
            self.logger.error(f'{username} is not logged in', str(e), exc_info=True)

    def check_login_into(self):
        try:
            self.logger.info('check that the user is logged in system')
            assert 'logged in user session' in self.response['message'], 'we dont received message'
            self.logger.info('check passed')

        except AssertionError as e:
            self.logger.error("assert verification failed", e, exc_info=True)

    def login_out(self, some_name: str):
        try:
            self.logger.info(f"log out user {some_name}")
            self.response = requests.get('https://petstore.swagger.io/v2/user/logout')

        except requests.exceptions.RequestException as e:
            self.logger.error(f"User {some_name} in system", e, exc_info=True)
    def assert_email(self, email):
        try:
            assert self.response['email'] == email
            self.logger.info("email verification passed")
        except AssertionError as e:
            self.logger.info("email verification failed", e, exc_info=True)

    def assert_user_name(self, some_user_name):
        try:
            assert self.response['username'] == some_user_name
            self.logger.info("username verification passed")
        except AssertionError as e:
            self.logger.info("username verification failed", str(e), exc_info=True)

    def asser_password(self, password):
        try:
            assert self.response['password'] == password
            self.logger.info("password verification passed")
        except AssertionError as e:
            self.logger.info("password verification failed", str(e), exc_info=True)
