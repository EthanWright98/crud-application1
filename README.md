# Festival Planner

<br>
<br>
<br>
<br>

## Objectives

The objective for this project was to create a simple CRUD application (Create, Read, Update and Delete).

In this project i showcases my ability to:

- Show python skills to create a Functional CRUD application
- Create two databases with a one to many relationship
 - The use of Jenkins and pytest to test my application and provide a coverage report
 - Deploy my application using a VM (GCP)
<br>
<br>
<br>
## My Application

My application idea was to create a festival planner in which you can; 

- Enter a festival name
- Enter a festival start date
- Enter a festival end date
- Enter a stage names for the stated festival
- edit/update festival and stages
- Delete festivals and stages

This idea is a one to many relationship between two tables being one festival can have many stages but a stage can only belong to one festival. This table relationship can be displayed through an ERD (Entity relationship diagram)
<br>
<br>
<br>
![screenshot](Capture%20ERD.PNG)
<br>
<br>
<br>
## risk assesment
<br>
For this project i created a risk assesment to show potential threats and at which level they would impact my work, i was able to use the risk assesment to create a more secure app through mitigation and responses to threats.
<br>
<br>
<br>

![screenshot](Risk%20assesment%202.PNG)

## Project Tracking
<br>
In order to track progess for my project, see goals and meet the MVP i used trello to create a board displaying requirements and keeping me up to schedule. Elements of the prject move across the baord left to right from the idea up until being finished and impletmented into the project
<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/101715806/163796114-41870b38-aed0-4f74-b49c-4b9a40c4c389.png)

<br>
<br>
<br>

## jenkins Testing and CI pipeline
<br>
<br>
Jenkins was implemted into my project to provide reports and automate testing of code, a webhook was also set up to mirror changes made within the github repository into the jenkins system. Below are the instructions i gave jenkins within the execute shell in order for it to be able to create a virtual environment and install requirements needed for the applcation to run.
<br>
<br>
#!/bin/bash<br>
python3 -m venv venv<br>
. ./venv/bin/activate<br>
pip3 install -r requirements.txt<br>
pip3 install pytest<br>
pip install pytest-cov<br>
python3 -m pytest --cov=application --cov-report term-missing
<br>
<br>

![image](https://github.com/EthanWright98/crud-application1/blob/main/Capture1%20jenkins%20test.PNG)

## Unit Testing
<br>
<br>
Unit testing was carried out within the app to help ensure functionality that was implemted was working as intended and that chnages created through user input would not cause my application to crash or error.
<br>
<br>
<br>

![image](https://github.com/EthanWright98/crud-application1/upload/main)

