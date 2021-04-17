import base64
import json
import requests
from requests_http_signature import HTTPSignatureAuth

class LibZeta:
    
    def __init__(self, url, key, key_id):
        self.url= url
        self.key = key
        self.key_id = key_id

    def create_user(self, username:str):
        response = requests.get(
            url=f"{self.url}/user/{username}",
            auth= HTTPSignatureAuth(
                key=self.key, 
                key_id=self.key_id,
            )
        )
        if response.status_code == 200:
            return response.json()['user_info']
        raise Exception(response.text)

        fake_response ={
            'client': 'test-app', 
            'user_info': {
                'username': username, 
                'token': '$2b$10$4l9ttuSH.hPH/SsbKas4sOZ8tKpHPGyL/sB4OzZhB0Q.bcnFmH04u', 
                'profiles': ['user', 'orderManagement', 'mailNotifications']
            }
        }
        return fake_response['user_info']

    def verify_user(self, username:str, token:str):
        token = str(base64.b64encode(token.encode('utf-8')), 'utf-8')
        response = requests.post(
            url=f"{self.url}/verify/{username}/{token}",
        )
        if response.status_code == 200:
            return response.json()['user_info']
        raise Exception(response.text)

        fake_response = {
            'client': 'test-app', 
            'user_info': {
                'username': username, 
                'token': '$2b$10$4l9ttuSH.hPH/SsbKas4sOZ8tKpHPGyL/sB4OzZhB0Q.bcnFmH04u', 
                'valid': True
                }
        }
        return fake_response['user_info']