import pytest
import random
import string
import requests

from methods.pet_methods import PetMethods


@pytest.fixture()
def pet_methods():
    return PetMethods()

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@pytest.fixture()
def unique_user_data():
    general_id = random.randint(100000, 999999)
    category_id = random.randint(1,9)
    category_name = generate_random_string(10)
    pet_name = generate_random_string(8)
    photo_urls = generate_random_string(15)
    tag_id = random.randint(1, 9)
    tag_name = generate_random_string(6)

    payload = {
        'id': general_id,
        'category': {
            'id': category_id,
            'name': category_name
        },
        'name': pet_name,
        'photoUrls': [
            photo_urls
        ],
        'tags': [
            {
                'id': tag_id,
                'name': tag_name
            }
        ],
        'status': 'available'
    }

    return payload
