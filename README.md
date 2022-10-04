# JobWallet2
Digital traceability app for a manufacturing environment

## Application objective
The project came to live to help with serial number and operations tracability in a manufacturing enviroment. The pen and paper method was ineffective and a database model seemed to be an ideal solution as it provides instant search options. The aim is to give the operators a tool for quick and easy way of recording which parts and when have been processed.

## Challange
The user interface has to be as simple and minimalistic as possible so the data input would be very easy and take as little time as possible. I tried to find the ways to auto fill as many information as possible. The application uses the logged in user as the person who "signs" the operation. It also records time and date of the signature. The parts can be recognized and called by serial number or an "FG" (project) code.

## Tools used
The project has been built with Django framework. It also utilises Bootstrap4

## To do
Next thing to do is an ability of inputting multiple parts at a time. At the moment the input of each part has to be confirmed with the "sign" button.

## How to run
In the main application folder run:

python manage.py runserver 

To create admin account run:

python manage.py createsuperuser


Demo
https://piotrzet.pythonanywhere.com/records/
