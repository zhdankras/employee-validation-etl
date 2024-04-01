import time
from repository.bamboohr_repository import BamboohrRepository
from repository.atlassian_repository import AtlassianRepository

class AtlassianValidation:

    def upload_validation_list(employee=None) -> list: 
        list_for_upload = list()

        employees_from_bamboohr = BamboohrRepository.get_employees_bamboo_data()
        
        if employee in employees_from_bamboohr: 
            status = []
            employee_from_atlassian = AtlassianRepository(email=employee).get_employee_atlassian_data()
            
            if employee_from_atlassian.status_code == 200:
                
                if len(employee_from_atlassian.json()) > 0:
                    
                    if employees_from_bamboohr.get(employee)[0] != employee_from_atlassian.json()[0].get('displayName'): 
                        status.append("The real name in Atlassian(Jira + Confluence) does not meet the standard!")
                    
                    if employee_from_atlassian.json()[0].get('avatarUrls').get('48x48').find("secure.gravatar.com") != -1: 
                        status.append("Profile without photo!")

                    if len(status) == 0:
                        status.append("Success!")

                    status_to_string = ""
                    list_for_upload.append(status_to_string.join(status))
                
                else:
                    list_for_upload.append("Not Found")
            
            elif employee_from_atlassian.status_code == 429:
                
                if 'Retry-After' in employee_from_atlassian.headers:
                    retry_after = int(employee_from_atlassian.headers['Retry-After'])
                    time.sleep(retry_after)
                
                else:
                    time.sleep(5)
            
        return list_for_upload

    