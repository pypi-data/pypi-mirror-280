
# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.


from .auth import AuthOperation
from .read_id import ReadIdOperation
import json 

class DatasetOperation:
    """
    A client for interacting with PowerBI API.
    """

    @staticmethod
    def get_ds(workspaceId, ds_name):
        """
        Retrieve a dataset ID based on its name within a workspace.

        :param workspaceId: ID of the workspace.
        :param ds_name: Dataset name.
        :return: Dataset ID.
        """
        read_id_operation = ReadIdOperation()
        auth_operation = AuthOperation()
        url = f"{auth_operation.BASE_URL}{workspaceId}/datasets/"
        return read_id_operation.get_id_from_name(url, ds_name)  # Asumiendo que ReadIdOperation tiene un método llamado get_id_from_name
    
    @staticmethod
    def get_all(workspaceId):
        """
        Retrieve a dataset ID based on its name within a workspace.

        :param workspaceId: ID of the workspace.
        :param ds_name: Dataset name.
        :return: Dataset ID.
        """
        read_id_operation = ReadIdOperation()
        auth_operation = AuthOperation()
        url = f"{auth_operation.BASE_URL}{workspaceId}/datasets/"
        return read_id_operation.get_all(url)  # Asumiendo que ReadIdOperation tiene un método llamado get_id_from_name
    

    @staticmethod
    def dax_query(workspaceId, datasetId, query):
        """
        Retrieve a dataset ID based on its name within a workspace.

        :param workspaceId: ID of the workspace.
        :param ds_name: Dataset name.
        :return: Dataset ID.
        """
        read_id_operation = ReadIdOperation()
        auth_operation = AuthOperation()
        url = f"{auth_operation.BASE_URL}{workspaceId}/datasets/{datasetId}/executeQueries"
        body = {
            "queries": [
                {
                "query": query  # Use the static query
                }
            ],
            "serializerSettings": {
                "includeNulls": "true"
            },
            "impersonatedUserName": "someuser@mycompany.com"	
        }
        body = json.dumps(body)
        return read_id_operation.get_all(url, body=body)  # Asumiendo que ReadIdOperation tiene un método llamado get_id_from_name

