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
To run this app you will need python3.10 installed on your system.

Create a new folder for the application and move into that folder:

```mkdir <folder_name> && cd <folder_name>```

Clone the git repo:

```git clone git@github.com:PiotrZettt/JobWallet2.git```

Create a virtual environment for the project:

```python3 -m venv <your_env_name>```

Change directory to the JobWallet Django app:

```cd JobWallet```

Install all requirements by:
```pip install -r requirements.txt```

Before you create a database and run the server you will need to create a secret key by exporting an environmental variable. It will be read and used by Django's settings.py

```export SECRET_KEY="<Use_a_string_here>"```

We can create a database now:

```python manage.py makemigrations```  
```python manage.py migrate```

You will also need an admin account. Use command:

```python manage.py createsuperuser```

and follow the prompts.
Everything's ready now. Run the app by:

```python manage.py runserver```

The app should open in your browser on http://127.0.0.1:8000/  

Demo
https://piotrzet.pythonanywhere.com/records/
