# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.



import requests
from azure.identity import ClientSecretCredential
from .base import BaseOperation
from .auth import AuthOperation
import requests
from .services.graph import GraphAPI



class CapacityAutomation(dict):
    def __init__(self, details, auth_headers, credential, email_list=None, send_notification=False, language="en"):
        super().__init__(details)
        self._details = details

        self.name = details["displayName"]
        self.auth_headers = auth_headers
        self.base_url = "https://management.azure.com"
        self.graph_client = GraphAPI(credential=credential)
        self.email_list = email_list if email_list else []
        self.send_notification = send_notification
        self.language = language

    def suspend(self):
        operation = "suspend"
        response = self.perform_operation(operation)
        return response

    def resume(self):
        operation = "resume"
        response = self.perform_operation(operation)

        return response

    def perform_operation(self, operation):
        response = requests.post(url=f"{self.base_url}{self.graph_client.get_resource_info(service_name=self.name)}/{operation}?api-version=2022-07-01-preview", headers=self.auth_headers)

        self.send_notification_email(response, operation)
        return response

    def send_notification_email(self, response, operation):
        subject, body = self.get_email_content(operation, response)
        for email in self.email_list:
             self.graph_client.send_email(
                subject=subject,
                body=body,
                to=email
            )

    def get_email_content(self, operation, response):
        if operation == "suspend":
            operation_en = "shutdown"
            operation_es = "apagado"
        elif operation == "resume":
            operation_en = "startup"
            operation_es = "encendido"
        else:
            operation_en = operation
            operation_es = operation
    
        if response.status_code in [200, 202]:
            if self.language == "en":
                return f"Capacity {self.name} {operation_en}", f"The capacity {self.name} has been {operation_en} successfully. Status code: {response.status_code}"
            else:  # Assume Spanish if not English
                return f"Capacidad {self.name} {operation_es}", f"La capacidad {self.name} ha sido {operation_es} correctamente. Código de estado: {response.status_code} - {response.text}"
        else:
            if self.language == "en":
                return f"Capacity {self.name} {operation_en}", f"An error occurred during the {operation_en} of capacity {self.name}. Status code: {response.status_code}"
            else:  # Assume Spanish if not English
                return f"Capacidad {self.name} {operation_es}", f"Ocurrió un error durante el proceso de {operation_es} de la capacidad {self.name}. Código de estado: {response.status_code} - {response.text}"

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"'Capacity' object has no attribute '{item}'")

    def __repr__(self):
        return str(self._details)


class CapacityOperation(BaseOperation):
    def __init__(self, auth_operation):
        self.management_auth = AuthOperation(api_scope='management', auth_type=auth_operation.auth_type, client_id=auth_operation.client_id, tenant_id=auth_operation.tenant_id, client_secret=auth_operation.client_secret)
        super().__init__(auth_operation)
        self.auth_headers, self.credential = self._authenticate()

    def _authenticate(self):
        token = self.management_auth.token
        headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {token}"}
        credential = ClientSecretCredential(tenant_id=self.management_auth.tenant_id, client_id=self.management_auth.client_id, client_secret=self.management_auth.client_secret)
        return headers, credential

    def list(self):
        response = self.get("/admin/capacities?$expand=tenantKey")
        return response["value"]

    def get_by_name(self, name):
        capacities = self.list()
        for capacity in capacities:
            if capacity.get("displayName") == name:
                return capacity
        return None

    def get_by_id(self, resource_id):
        capacities = self.list()
        for capacity in capacities:
            if capacity["id"] == resource_id:
                return capacity
        return None