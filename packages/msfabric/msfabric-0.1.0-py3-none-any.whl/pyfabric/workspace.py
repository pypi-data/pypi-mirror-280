
# Author: Jonathan Cuéllar Viveros
# Company: Dalatic S.L
# Contact: info@dalatic.com
# Copyright (C) 2024 Jonathan Cuéllar Viveros. All rights reserved.
# Derechos de autor (C) 2024 Jonathan Cuéllar Viveros. Todos los derechos reservados.


from .auth import AuthOperation
from .base import BaseOperation

class WorkspaceOperation(BaseOperation):
    def __init__(self, auth_operation=None):
        if auth_operation is None:
            auth_operation = AuthOperation(auth_type='service_principal')
        super().__init__(auth_operation)
    
    def list_workspaces(self):
        response = self.get("/myorg/groups")
        return response["value"]

    def get_workspace_by_name(self, name):
        workspaces = self.list_workspaces()
        for workspace in workspaces:
            if workspace.get("name") == name:
                return workspace
        return None

    def get_workspace_by_id(self, workspace_id):
        workspaces = self.list_workspaces()
        for workspace in workspaces:
            if workspace["id"] == workspace_id:
                return workspace
        return None
