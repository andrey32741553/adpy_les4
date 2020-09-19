import unittest
from les4_task2.les4_task2_adpy import create_folder_on_yadisc, folder, ya_token
import requests



class Test_les4_task2(unittest.TestCase):

    def setUp(self):
        print('setup method')


    def tearDown(self):
        print('teardown method')


    def test_create_folder_on_yadisc(self):
        response = requests.get(
            'https://cloud-api.yandex.net:443/v1/disk/resources',
            params={
                'path': f'{folder}'
            },
            headers={
                'Authorization': ya_token
            }
        )
        self.assertEqual(create_folder_on_yadisc(), folder)