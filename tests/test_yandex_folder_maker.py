import unittest
import requests
from yandex_folder_maker import create_folder, _get_token

class TestGettingTokens(unittest.TestCase):
    correct_path = "config.env"
    def test_path_not_str(self):
        self.assertRaises(TypeError, _get_token, True)
    
    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, _get_token, 'wrong/way')

    @unittest.expectedFailure
    def test_gets_access_to_correct_config_file(self):
        self.assertRaises(FileNotFoundError, _get_token, self.correct_path)

    def test_correct_getting_token(self):
        assert _get_token(self.correct_path)[:2] == 'y0'
    

class TestYandexAPI(unittest.TestCase):
    testing_folder_name = 'folder_name_1'
    default_ya_headers = {
        "Authorization": _get_token("config.env"),
        "Content-Type": "application/json", 
    }
    token = default_ya_headers.get("Authorization")

    def tearDown(self):
        url_delete = "https://cloud-api.yandex.net/v1/disk/resources"
        params_delete = {
            "path": self.testing_folder_name,
        }
        requests.delete(
            url=url_delete,
            params=params_delete,
            headers=self.default_ya_headers,
        )
        
    def test_creating_folder(self):
        response = create_folder(
            folder_name=self.testing_folder_name,
            token=self.token
        )

        self.assertEqual(response.status_code, 201)
        response = requests.get(
            url="https://cloud-api.yandex.net/v1/disk/resources/",
            headers=self.default_ya_headers,
            params={
                'path': self.testing_folder_name
            }
        )
        self.assertEqual(response.json().get('name', None), self.testing_folder_name)


    def test_error_making_same_folder_again(self):
        response = create_folder(
            folder_name=self.testing_folder_name,
            token=self.token
        )

        self.assertEqual(response.status_code, 201)

        response = create_folder(
            folder_name=self.testing_folder_name,
            token=self.token
        )

        self.assertEqual(response.status_code, 409)
    
    def test_wrong_token(self):
        response = create_folder(
            folder_name=self.testing_folder_name,
            token="wrong_token",
        )

        self.assertEqual(response.status_code, 401)

    def test_wrong_folder_name_type(self):
        self.assertRaises(TypeError, create_folder, True, self.token)
