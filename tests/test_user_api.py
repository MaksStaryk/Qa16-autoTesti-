import allure
from services.user_API import UserService
from data.other_dict_for_tests.user_dict import *


@allure.title('путь от создания, обновления пользователя до удаления пользователя')
def test_user():
    create_user = UserService()
    create_user.create_user(user_01)
    create_user.get_information('Maxim')
    create_user.assert_email('sg@gmail.com')
    create_user.asser_password('qwert')
    create_user.update_information('Maxim', user_01_v2)
    create_user.get_information('Maximus')
    create_user.asser_password('qwerty123')
    create_user.enter_system('Maximus', 'qwerty123')
    create_user.check_login_into()
    create_user.login_out('Maximus')
    create_user.delete_user('Maximus')
    create_user.check_delete('Maximus')
