import allure
from services.user import UserService1
from services.other_dict_for_tests.user_dict import *


@allure.feature('create user1')
def test_create_user():
    create_user = UserService1()
    create_user.create_user(user_01)
    create_user.get_information('Maxim')
    create_user.assert_email('sg@gmail.com')
    create_user.asser_password('qwert')
    create_user.update_information('Maxim', user_01_v2)
    create_user.get_information('Maximus')
    create_user.asser_password('qwerty123')
    create_user.delete_user('Maximus')
    create_user.check_delete('Maximus')


