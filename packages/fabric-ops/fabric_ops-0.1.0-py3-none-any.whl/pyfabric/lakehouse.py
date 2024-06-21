# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.


import json
from .auth import AuthOperation
from .base import BaseOperation

class LakeHouseOperation(BaseOperation):
    """
    A client for interacting with LakeHouse API.
    """
    def __init__(self):
        super().__init__(AuthOperation())
        self.base_url = "https://api.fabric.microsoft.com/v1/"


    def load_data(self, workspaceId, lakehouseId, relativePath, mode="overwrite", delimiter=",", format="CSV"):
        """
        Load data into a lakehouse table.
        """
        url = f"{self.base_url}workspaces/{workspaceId}/lakehouses/{lakehouseId}/tables/demo/load"
        body = {
            "relativePath": relativePath,
            "pathType": "File",
            "mode": mode,
            "formatOptions": {
                "header": True,
                "delimiter": delimiter,
                "format": format
            }
        }
        body = json.dumps(body)
        return self.post(url, body=body)

    def list_tables(self, workspaceId, lakehouseId, maxResults=None):
        """
        List tables in a lakehouse.
        """
        url = f"{self.base_url}workspaces/{workspaceId}/lakehouses/{lakehouseId}/tables"
        if maxResults is not None:
            url += f"?maxResults={maxResults}"
        return self.get(url)

    def get_properties(self, workspaceId, lakehouseId):
        """
        Get properties of a lakehouse.
        """
        url = f"{self.base_url}workspaces/{workspaceId}/lakehouses/{lakehouseId}"
        return self.get(url)