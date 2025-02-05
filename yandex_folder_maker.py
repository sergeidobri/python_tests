import requests
import os
from dotenv import load_dotenv

def _get_token(path_to_conf="config.env"):
    if type(path_to_conf) is not str:
        raise TypeError("Путь к файлу следует прописывать в виде строки")
    
    if os.path.exists(path_to_conf):
        load_dotenv(path_to_conf)
    else:
        raise FileNotFoundError("Файл не был найден")
    
    return os.getenv("YA_TOKEN")

def create_folder(folder_name, token):
    if type(folder_name) is not str:
        raise TypeError("Название папки следует прописывать в виде строки")

    url_folder_create = 'https://cloud-api.yandex.net/v1/disk/resources'
    params_folder_create = {
        "path": f"{folder_name}/",
    }
    headers_folder_create = {
        "Authorization": token,
        "Content-Type": 'application/json',
    }
    response = requests.put(
        url=url_folder_create,
        params=params_folder_create,
        headers=headers_folder_create,
    )

    return response

if __name__ == '__main__':
    create_folder('test_folder', _get_token())