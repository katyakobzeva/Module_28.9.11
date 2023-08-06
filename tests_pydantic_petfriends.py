from typing import Dict

from pydantic import BaseModel
import pytest
import requests


class GetApiKey(BaseModel):
    key: str

class User(BaseModel):
    email: str
    password: str

def test_get_api_key():
    request = {
        "key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae72"
    }
    GetApiKey(**request)

def test_users_get_api_key():
    response = [
        {"email": "test@02test@bk.ru", "password": "123456789"}
    ]
    users = [User(**user) for user in response]

def test_get_api_key():
    request = {}
    with pytest.raises(ValueError):
        GetApiKey(**request)

class Post_CreatePetSimple(BaseModel):
    auth_key: str
    name: str
    animal_type: str
    age: int

def test_api_create_pet_simple():
    response = [
        {"auth_key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae72",
         "name": "Mimi",
         "animal_type": "dog",
         "age": "3"}
    ]
    new_pet = [Post_CreatePetSimple(**user) for user in response]
    assert new_pet[0].name == "Mimi"
    assert new_pet[0].animal_type == "dog"
    assert new_pet[0].age == 3

def test_post_pet_simple():
    request = {}
    with pytest.raises(ValueError):
        Post_CreatePetSimple(**request)

class New_information_pet(BaseModel):
    auth_key: str
    pet_id: str
    name: str
    animal_type: str
    age: int

def test_put_new_information_pet():
    response = [
        {"auth_key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae72",
         "pet_id": "f3043661-b5a7-41b2-be7c-39e1e3141290",
         "name": "Мурка",
         "animal_type": "кошка",
         "age": "5"}
    ]
    new_info = [New_information_pet(**user) for user in response]
    assert new_info[0].name == "Мурка"
    assert new_info[0].animal_type == "кошка"
    assert new_info[0].age == 5

class DeletePet(BaseModel):
    auth_key: str
    pet_id: str

def test_delete_pet():
    response = [
        {"auth_key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0ae72",
         "pet_id": "f3043661-b5a7-41b2-be7c-39e1e3141290",
         }
    ]
    pet  = [DeletePet(**user) for user in response]


