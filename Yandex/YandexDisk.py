import json
import os
from urllib.parse import urlencode

import webbrowser
import requests


class YandexToken:
    """Класс для получения токена пользователя Яндекса"""

    # Получение абсолютного пути до текущего файла
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Получение абсолютного пути до YandexAppInfo.json
    app_info_path = os.path.join(current_dir, "YandexAppInfo.json")

    with open(app_info_path, "r") as id:
        APP_ID = json.load(id).get("APP_ID")
    base_url = "https://oauth.yandex.ru/authorize"
    params = {"client_id": APP_ID, "response_type": "token"}

    token_path = os.path.join(current_dir, "yandex_token.json")

    def get_user_token(self):
        if os.path.exists(self.token_path):
            with open(self.token_path, "r") as token:
                access_token = json.load(token).get("token")
        else:
            link = f"{self.base_url}?{urlencode(self.params)}"
            print(
                "Для доступа к Яндекс Диску перейдите по ссылке, авторизуйтесь, "
                "скопируйте URL в адресной строке браузера и вставьте ниже"
            )
            print(link)
            webbrowser.open_new_tab(link)
            user_url = input("Вставьте ссылку: ")
            if user_url.find("access_token=") != -1:
                access_token = user_url[
                    user_url.find("access_token=")
                    + len("access_token=") : user_url.find("token_type")
                    - 1
                ]

            else:
                access_token = user_url
            info = {"token": access_token}
            with open(self.token_path, "w") as token:
                token.write(json.dumps(info))
        return access_token


class YandexDisk:
    """Класс описывает методы загрузки фотографий на яндекс диск"""

    # Получение абсолютного пути до текущего файла
    current_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(current_dir, "yandex_token.json")

    def __init__(self):
        self.BASE_YA_URL = "https://cloud-api.yandex.net/v1/disk/resources"
        with open(self.token_path, "r") as token:
            self.access_token = json.load(token).get("token")
        self.headers = {"Authorization": self.access_token}

    def create_folder(self, folder_name):
        self.params = {"path": folder_name}
        response = requests.put(
            f"{self.BASE_YA_URL}", params=self.params, headers=self.headers
        )
        if "error" in response.json():
            pass
        return response
