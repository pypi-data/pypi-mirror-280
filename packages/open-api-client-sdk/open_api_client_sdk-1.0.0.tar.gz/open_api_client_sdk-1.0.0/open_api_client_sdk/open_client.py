# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-05-21
 @File: open_client.py
 @Description: 
"""

import requests
import hashlib
import time
import random


class OpenClient:
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret

    def generate_sign(self, parameter):
        return hashlib.md5((parameter + "." + self.app_secret).encode('utf-8')).hexdigest()

    def get_name_by_get(self, name):
        try:
            url = f'http://127.0.0.1:9002/api/user/get?name={name}'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(f'Name: {data["name"]}')
        except requests.RequestException as e:
            print(f'Error: {e}')

    def get_name_by_post(self, name):
        try:
            url = 'http://127.0.0.1:9002/api/user/post'
            data = {'name': name}
            headers = {
                'Content-Type': 'application/json',
                'appKey': self.app_key,
                'parameters': str(data),
                'timestamp': str(int(time.time())),
                'nonce': str(random.randint(0, 1000000)),
                'sign': self.generate_sign(str(data))
            }
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            data = response.json()
            print(f'Name: {data["name"]}')
        except requests.RequestException as e:
            print(f'Error: {e}')
