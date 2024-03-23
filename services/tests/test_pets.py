from services.pets.create_pet import CreatePet
from services.pets.delete_pet import DeletePet
from services.pets.get_inf_pet import GetPet
from services.pets.update_pet import UpdatePet
from services.other_dict_for_tests.pets_dict import *


def test_create_pet():
    create_pet = CreatePet()
    create_pet.add_pets(information)
    create_pet.check_cod_200()
    create_pet.check_name('Harvey')
    create_pet.add_photo(787, r"C:\Users\Admin\PycharmProjects\Qa16-autoTesti-\services\foto\FELV-cat.jpg")
    create_pet.check_add_photo()


def test_get_pet():
    get_pet = GetPet()
    get_pet.get_pet(787)
    get_pet.check_cod_200()
    get_pet.assert_name('Mercedes')


def test_update_pet():
    update_pet = UpdatePet()
    update_pet.update_inf(information_v_2)
    update_pet.check_cod_200()
    update_pet.assert_information_name('Doggie')


def test_get_update_inf():
    get_update = GetPet()
    get_update.get_pet(787)
    get_update.check_cod_200()
    get_update.assert_name('Boxer')


def test_delete_pet():
    delete_pet = DeletePet()
    delete_pet.delete_pet(787)
    delete_pet.check_cod_200()
    check_pet = GetPet()
    check_pet.get_pet(787)
    check_pet.status_404()
