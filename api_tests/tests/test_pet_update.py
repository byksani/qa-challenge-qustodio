import pytest
import requests

from api_tests.data import SystemMessages, Urls


class TestUpdatePet:
    def test_update_pet_valid_payload_success_result(self, pet_methods, unique_user_data):
        pet_methods.create_pet(unique_user_data)

        status_code, response_context = pet_methods.edit_pet(unique_user_data)

        assert status_code == 200, \
            f'Expected status 200, but got {status_code}.'

        assert response_context == unique_user_data, \
            'Response body does not match the updated payload.'

    def test_update_pet_empty_payload_error_405(self, pet_methods):
        status_code, response_context = pet_methods.edit_pet(None)

        assert status_code == 405, \
            f'Expected status 405, but got {status_code}.'

        assert response_context['message'] == SystemMessages.NO_DATA, \
            f"Expected error message '{SystemMessages.NO_DATA}', but got '{response_context['message']}'."

    def test_update_pet_with_empty_body_returns_valid_structure(self, pet_methods):
        status_code, response_context = pet_methods.edit_pet({})

        assert status_code == 200, \
            f"Expected status 200 (API allows empty payload), but got {status_code}."

        assert 'id' in response_context, "Missing 'id' in response"
        assert response_context['photoUrls'] == [], "'photoUrls' should be empty list"
        assert response_context['tags'] == [], "'tags' should be empty list"

    def test_update_pet_with_text_plain_content_type_returns_415(self):
        payload = '{"id": 123}'
        headers = {"Content-Type": "text/plain"}

        response = requests.put(Urls.BASE_URL, data=payload, headers=headers)

        assert response.status_code == 415, \
            f"Expected status 415, but got {response.status_code}."
