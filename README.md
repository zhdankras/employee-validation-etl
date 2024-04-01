# Employee Profile Validation (serverless) 
## How it works?
Automation works like this: there is a special Google Sheet document that stores information about all employees who are on BambooHR:
Every week, the contents of the table are automatically updated using our serverless application, which we developed to clean and populate the table with new
data. The table has the following columns:
1) **All accounts** – the column contains all accounts that are in the system BambooHR;
2) **Services** – the column contains the services that are used to verify the basic data that must be filled in the employee profile;
3) **BambooHR** – this column contains the first and last names of all employees. This is the key column by which the employee's first and last names are verified in individual services;
4) **Google** – the column contains certain metrics and the corresponding checkbox system for checking employee profiles in the Google Workspace service;
5) **Slack** – the column contains certain metrics and the corresponding checkbox system for checking user profiles in the Slack service;
6) **Atlassian(Jira + Confluence)** – the column contains certain metrics and the corresponding checkbox system for checking user profiles
in the Atlassian(Jira + Confluence) service;</br>
---
At the end of each week, a notification is sent to the Slaсk channel about updated information:
<p align="center"><img width="799" alt="Screenshot 2024-04-01 at 8 02 27 PM" src="https://github.com/zhdankras/employee-validation-etl/assets/55245041/6e059868-85a4-4f39-b7f4-60fcffbf9d59"></p>


