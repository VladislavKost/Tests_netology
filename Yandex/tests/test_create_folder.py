import os
import json
import unittest
from Yandex.YandexDisk import YandexToken, YandexDisk


class TestYandexDisk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = YandexToken()
        token.get_user_token()
        cls.folder = YandexDisk()
        cls.folder_name = "tessdfsadft"
        yandex_dir = os.path.abspath(os.path.join(__file__, "../.."))
        cls.token_path = os.path.join(yandex_dir, "yandex_token.json")

    def test_1_folder_creation_new(self):
        response = self.folder.create_folder(self.folder_name).status_code
        self.assertEqual(response, 201, "Папка не создана, проверьте имя папки")

    def test_2_second_creation(self):
        response = self.folder.create_folder(self.folder_name).status_code
        self.assertEqual(
            response, 409, "Папка с таким именем не была создана в предыдущем тесте"
        )

    def test_3_authorization_error(self):
        info = {"token": "No token"}
        with open(self.token_path, "w") as token:
            token.write(json.dumps(info))
        self.new_folder = YandexDisk()
        response = self.new_folder.create_folder(self.folder_name).status_code
        self.assertEqual(response, 401, "Не проишла проверка ошибки авторизации")
