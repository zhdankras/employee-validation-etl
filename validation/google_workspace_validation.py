from repository.bamboohr_repository import BamboohrRepository
from repository.google_workspace_repository import GoogleWorkspaceRepository

class GoogleWorkspaceValidation:

    def __init__(self, credentials):
        self.credentials = credentials

    def upload_validation_list(self, employee) -> list: 
        list_for_upload = list()
        employees_from_bamboohr = BamboohrRepository.get_employees_bamboo_data()
        employees_from_google_workspace = GoogleWorkspaceRepository(credentials=self.credentials).get_employees_google_workspace_data()
        
        if employee in employees_from_bamboohr: 
            
            if list(employees_from_google_workspace.keys()).count(employee) > 0:
                
                if employees_from_bamboohr.get(employee)[0] == employees_from_google_workspace.get(employee):
                    list_for_upload.append('✓')
                
                else:
                    list_for_upload.append('✕')
            
            else:
                list_for_upload.append('Not Found')
        
        return list_for_upload
