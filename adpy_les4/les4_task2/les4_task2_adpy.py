import requests

folder = 'test_folder'

ya_token = # Ваш токен


def create_folder_on_yadisc():
    requests.put('https://cloud-api.yandex.net:443/v1/disk/resources',
                     params={
                         'path': folder
                     },
                     headers={
                         'Authorization': ya_token
                     }
                )
    response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources',
            params={
                'path': f'{folder}'
            },
            headers={
                'Authorization': ya_token
            }
        )

    if 'name' in response.json():
        folder_name = response.json()['name']
        return folder_name


if __name__ == '__main__':
    print(create_folder_on_yadisc())
