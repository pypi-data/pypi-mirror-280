# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.


import json
from azure.identity import ClientSecretCredential
from datetime import datetime, timedelta
import msal
import os

class AuthOperation:
    API_SCOPES = {
        'pbi': ['https://analysis.windows.net/powerbi/api/.default'],
        'fabric': ["https://api.fabric.microsoft.com/Workspace.ReadWrite.All", "https://api.fabric.microsoft.com/Item.ReadWrite.All"],
        'management': ["https://management.azure.com/.default"]
    }
    _token_expiry = None

    def __init__(self, api_scope='pbi', auth_type='service_principal', client_id=None, tenant_id=None, client_secret=None):
        self.api_scope = api_scope
        self.auth_type = auth_type
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.client_secret = client_secret
        self._token = None
        self._fetch_secrets()
        self._authenticate()

    def _fetch_secrets(self):
        if not all([self.client_id, self.tenant_id, self.client_secret]) and os.getenv("MSFABRIC_EMAIL_SENDER"):
            pbi_config = json.loads(os.getenv("MSFABRIC_CONF"))
            self.client_id = pbi_config.get('client_id')
            self.tenant_id = pbi_config.get('tenant_id')
            self.client_secret = pbi_config.get('client_secret')
            self.storage_account_name = pbi_config.get('storage_account_name')

    
    def _authenticate(self):
        try:
            if self.auth_type == 'service_principal':
                auth = ClientSecretCredential(
                    tenant_id=self.tenant_id,
                    client_id=self.client_id,
                    client_secret=self.client_secret
                )
                token_response = auth.get_token(*self.API_SCOPES[self.api_scope])
                self._token = token_response.token
            elif self.auth_type == 'client_app' or self.api_scope == "fabric":
                public_client_app = msal.PublicClientApplication(
                    client_id=self.client_id,
                    authority=f"https://login.microsoftonline.com/{self.tenant_id}"
                )
                accounts = public_client_app.get_accounts()
                if accounts:
                    result = public_client_app.acquire_token_silent(*self.API_SCOPES[self.api_scope], account=accounts[0])
                else:
                    result = public_client_app.acquire_token_interactive(*self.API_SCOPES[self.api_scope])

                self._token = result['access_token']
                self._token_expiry = datetime.now() + timedelta(hours=1)
            else:
                raise ValueError(f"Invalid auth_type: {self.auth_type}")

            self._token_expiry = datetime.now() + timedelta(hours=1)
        except Exception as e:
            raise e

    @property
    def token(self):
        if datetime.now() >= self._token_expiry:
            self._authenticate()
        return self._token

    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
