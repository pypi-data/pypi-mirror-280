# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.



from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest
    
import requests
import json
import msal
import os
class GraphAPI:
    def __init__(self, credential):
        self.credential = credential
        self.resource_graph_client = ResourceGraphClient(self.credential)
        self.subscription_client = SubscriptionClient(self.credential)
        
    def list_subscriptions(self):
        subscriptions = self.subscription_client.subscriptions.list()
        subscription_ids = [sub.subscription_id for sub in subscriptions]
        return subscription_ids

    def get_resource_info(self, service_name):
        subscription_ids = self.list_subscriptions()
        query = f"""
        Resources
        | where type == 'microsoft.fabric/capacities'
        | where name == '{service_name}'
        | project id, name, type, subscriptionId
        """
        request = QueryRequest(
            subscriptions=subscription_ids,
            query=query
        )
        response = self.resource_graph_client.resources(request)
        if not response.data or len(response.data) == 0:
            raise ValueError(f"No resource found with the name {service_name}")
        
        resource_info = response.data[0]
        return resource_info["id"]




    def send_email(self, subject, body, to):
        # Check if 'to' is a list and convert it to a comma-separated string if necessary
        if isinstance(to, list):
            to = ', '.join(to)
    
        # Your application (client) ID and client secret obtained from Azure AD
        client_id = self.credential._client_id
        client_secret = self.credential._client_credential
    
        # Tenant ID (directory ID)
        tenant_id = self.credential._tenant_id
    
        # Microsoft Graph API endpoint to send an email as the application (service principal)
        sender = os.getenv("MSFABRIC_EMAIL_SENDER")
        graph_url = f"https://graph.microsoft.com/v1.0/users/{sender}/sendMail"
    
        # Create a confidential client application
        app = msal.ConfidentialClientApplication(
            client_id=client_id,
            authority=f"https://login.microsoftonline.com/{tenant_id}",
            client_credential=client_secret,
        )
    
        # Get an access token
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        access_token = result.get("access_token")
    
        # Create the email message
        email_message = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": body,
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient
                        }
                    } for recipient in to.split(', ')
                ]
               
            }
        }
    
        # Convert the message to JSON format
        email_data = json.dumps(email_message)
    
        # Send the email
        response = requests.post(
            graph_url,
            headers={
                "Authorization": "Bearer " + access_token,
                "Content-Type": "application/json",
            },
            data=email_data,
        )
    
        # Check the response status code
        if response.status_code != 202:
            raise Exception(f"Email send failed with status code {response.status_code}")