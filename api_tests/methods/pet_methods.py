import requests

from api_tests.data import Urls


class PetMethods:
    def create_pet(self, payload) -> tuple:
        headers = {"Content-Type": "application/json"}

        response = requests.post(Urls.BASE_URL, json=payload, headers=headers)
        return response.status_code, response.json()

    def edit_pet(self, payload) -> tuple:
        headers = {"Content-Type": "application/json"}

        response = requests.put(Urls.BASE_URL, json=payload, headers=headers)
        return response.status_code, response.json()
