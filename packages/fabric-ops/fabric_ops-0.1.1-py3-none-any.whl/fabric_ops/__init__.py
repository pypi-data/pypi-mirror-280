# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.
__version__ = "0.1.1"


from .auth import AuthOperation
from .capacity import CapacityOperation, CapacityAutomation

class Fabric:
    """
    English:
    The Fabric class is responsible for managing the authentication and capacity operations.

    Español:
    La clase Fabric es responsable de gestionar las operaciones de autenticación y capacidad.
    """
    def __init__(self, auth_operation=None, auth_type='service_principal', client_id=None, tenant_id=None, client_secret=None, email_list=None, send_notification=False, language="en"):
        """
        English:
        Initializes the Fabric class with the given parameters. If auth_operation is not provided, it is created with the provided auth_type, client_id, tenant_id, client_secret, username, and password. If client_id, tenant_id, or client_secret are not provided, they should be configured in an environment variable named MSFabricConf.

        Español:
        Inicializa la clase Fabric con los parámetros dados. Si no se proporciona auth_operation, se crea con el auth_type, client_id, tenant_id, client_secret, username y password proporcionados. Si no se proporcionan client_id, tenant_id o client_secret, deben estar configurados en una variable de entorno llamada MSFabricConf.
        """
        if not auth_operation:
            auth_operation = AuthOperation(api_scope='pbi', auth_type=auth_type, client_id=client_id, tenant_id=tenant_id, client_secret=client_secret)
        self.auth_operation = auth_operation
        self.fabric_capacity = CapacityOperation(auth_operation)
        self.email_list = email_list
        self.send_notification = send_notification
        self.language = language

    def capacity(self, *, name=None, resource_id=None):
   
        if name:
            capacity_data = self.fabric_capacity.get_by_name(name)
            if capacity_data:
                return CapacityAutomation(capacity_data, self.fabric_capacity.auth_headers, self.fabric_capacity.credential, self.email_list, self.send_notification, self.language)
            else:
                raise ValueError(f"Capacity with name {name} not found")
        elif resource_id:
            capacity_data = self.fabric_capacity.get_by_id(resource_id)
            if capacity_data:
                return CapacityAutomation(capacity_data, self.fabric_capacity.auth_headers, self.fabric_capacity.credential, self.email_list, self.send_notification, self.language)
            else:
                raise ValueError(f"Capacity with resource ID {resource_id} not found")
        else:
            raise ValueError("Either name or resource_id must be provided")
    
    def list_capacities(self):
        return self.fabric_capacity.list()
