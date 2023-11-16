from YandexDisk import YandexToken, YandexDisk


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    token = YandexToken()
    folder = YandexDisk()
    token.get_user_token()
    response = folder.create_folder("test").status_code
    print(response)
