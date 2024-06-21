# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.


import requests


class BaseOperation:
    def __init__(self, auth_operation):
        self.auth_operation = auth_operation
        self.url = "https://api.powerbi.com/v1.0/myorg"

    def post(self, relative_url, body):
        headers = self.auth_operation.headers()
        response = requests.post(self.url + relative_url, headers, json=body)
        response.raise_for_status()
        return response.json()

    def get(self, relative_url):
        headers = self.auth_operation.headers()
        response = requests.get(self.url + relative_url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def handle_response(self, response):
        if response.status_code in [200, 202]:
            print(f"Response status code: {response.status_code}")
        else:
            print(f"Response info: {response.json()}")