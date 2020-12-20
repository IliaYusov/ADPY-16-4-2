import pytest
import requests

def test_authorization_error(yandex_url):
    auth_header = {'Authorization': ''}
    kwargs = {'path': ''}
    response = requests.get(yandex_url, headers=auth_header, params=kwargs)
    assert response.status_code == 401

def test_create_folder(yandex_api_test_directory, yandex_api_token, folder_path, yandex_url):
    auth_header = {'Authorization': yandex_api_token}
    kwargs = {'path': folder_path}
    response = requests.get(yandex_url, headers=auth_header, params=kwargs)
    assert response.status_code == 200
