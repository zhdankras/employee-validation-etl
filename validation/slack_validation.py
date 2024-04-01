from repository.bamboohr_repository import BamboohrRepository
from repository.slack_repository import SlackRepository

class SlackValidation:

    def upload_validation_list(employee) -> list: 
        list_for_upload = list()
        employees_from_bamboohr = BamboohrRepository.get_employees_bamboo_data()
        employees_from_slack = SlackRepository.get_employees_slack_data()  
        
        if employee in employees_from_bamboohr: 
            
            if list(employees_from_slack.keys()).count(employee) > 0:   
                status = []
                if employees_from_slack[employee][0] != employees_from_bamboohr[employee][0]: 
                    status.append("The real name in Slack does not meet the standard!")

                if employees_from_slack[employee][1] != employees_from_bamboohr[employee][0]: 
                    status.append("The display name in Slack does not meet the standard!")

                if employees_from_slack[employee][2] == '': 
                    status.append("There is no description (position, where the person is from)!")

                if len(employees_from_slack[employee][2].split(', ')) == 3:
                    if (
                        employees_from_bamboohr[employee][1] == employees_from_slack[employee][2].split(', ')[1] and
                        employees_from_bamboohr[employee][2] == employees_from_slack[employee][2].split(', ')[2]
                    ): 
                        status.append("The location of the employee is set incorrectly(or the location not set at all)!")

                if employees_from_slack[employee][3] == '': 
                    status.append("Phone number not set!")

                if len(status) == 0:
                    status.append("Success!")
                    
                list_for_upload.append(status)
            
            else:
                list_for_upload.append("Not Found")
        
        return list_for_upload


