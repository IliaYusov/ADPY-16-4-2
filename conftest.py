import pytest
import os
import requests
from dotenv import load_dotenv

@pytest.fixture
def yandex_url():
    return 'https://cloud-api.yandex.net/v1/disk/resources'

@pytest.fixture
def yandex_api_token():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    return os.environ.get('YANDEX_TOKEN')

@pytest.fixture
def folder_path():
    return 'test_folder'

@pytest.fixture
def yandex_api_test_directory(yandex_api_token, folder_path, yandex_url):
    auth_header = {'Authorization': yandex_api_token}
    kwargs = {'path': folder_path}
    response_a = requests.put(yandex_url, headers=auth_header, params=kwargs)
    yield
    if response_a.status_code in (200, 201, 202, 204):
        response_b = requests.delete(yandex_url, headers=auth_header, params=kwargs)
