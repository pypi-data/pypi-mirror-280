# lom_api/client.py
import requests

class LomAPI:
    def __init__(self, base_url='https://www.lom-inc.jp'):
        self.base_url = base_url

    def authenticate(self, api_key):
        url = f'{self.base_url}/api/authenticate'
        response = requests.post(url, json={'api_key': api_key})
        response.raise_for_status()
        return response.json()

    def chat(self, user_id, message):
        url = f'{self.base_url}/chat/{user_id}'
        response = requests.post(url, json={'message': message})
        response.raise_for_status()
        return response.json()
