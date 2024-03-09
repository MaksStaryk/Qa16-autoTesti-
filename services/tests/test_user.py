from services.user.create_user import CreateUser
from services.other_dict_for_tests.user_dict import *
from services.user.delete_user import DeleteUser
from services.user.get_inf_user import GetUser
from services.user.login_into_system import Login
from services.user.update_inf import UpdateUser


def test_create_user():
    create_user = CreateUser()
    create_user.create_user(user_01)
    create_user.check_cod_200()


def test_get_inf_user():
    inf_user = GetUser()
    inf_user.get_inf('Maxim')
    inf_user.check_cod_200()
    inf_user.assert_email('sg@gmail.com')


def test_update_inf():
    update_inf = UpdateUser()
    update_inf.update_inf('Maxim', user_01_v2)
    update_inf.check_cod_200()
    user_new = GetUser()
    user_new.get_inf('Maximus')
    user_new.assert_user_name('Maximus')
    user_new.asser_password('qwerty123')


def test_login_into_out():
    login = Login()
    login.login_into('Maximus', 'qwerty13')
    login.check_cod_200()
    login.check_login_into()
    login.login_out()
    login.check_cod_200()


def test_delete_user():
    delete_user = DeleteUser()
    delete_user.delete_user('Maximus')
    delete_user.check_cod_200()
    check_delete = GetUser()
    check_delete.get_inf('Maximus')
