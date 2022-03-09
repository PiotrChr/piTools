import requests
import json


class Client:
    def get(self, url):
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception('Connection error!')

        return json.loads(response.text)

    def post(self, url, data, json_data):
        response = requests.post(url, data, json_data)

        if response.status_code != 200:
            raise Exception('Connection error!')

        return json.loads(response.text)
