import allure

from services.pets_API import PetService
from data.other_dict_for_tests.pets_dict import *


@allure.title('Path from creating, add foto a pet to deleting')
def test_pet_api():
    pet = PetService()
    pet.create_pet(information)
    pet.add_foto(787, 'data/FELV-cat.jpg')
    pet.get_pet(787)
    pet.assert_information('id')
    pet.assert_information('status')
    pet.update_infor(information_v_2)
    pet.assert_information('id')
    pet.assert_information('status')
    pet.delete_pet(787)
    pet.check_delete(787)
