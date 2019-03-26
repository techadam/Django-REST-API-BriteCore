## Django REST API Britecore
This project is a Django REST API in relation to the software engineering challenge at britecore which involves building a REST API that allow insurers to define their own custom data model for their risks

### Problem
BriteCore was created to work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult for BriteCore to work with different forms of insurance like Automobile Policies, Cyber Liability etc. Come up with a solution that allows insurers to define their own custom data model for their risks and should be able to create their own risk types and attach as many different fields as they would like.

### Solution & Approach
In order to tackle the above problem, Django and Django REST Framework was used to put into place a structured data model such that risk types, risk fields and field types were created individual models and Risks has a one to many relationships with risk fields and risk fields are also related to field types in a one to one relationship. This structure allows the users to have risk types associated with as many risk fields as possible.

### Prerequisites
Python
Django web framework
Django Rest Framework

### Setup
```bash
pip install pipenv
mkdir project_folder
cd project_folder
git clone https://github.com/techadam/Django-REST-API-BriteCore.git
pipenv shell
pipenv install requirements.txt
python manage.py createsuperuser
python manage.py runserver
# Running the tests
python manage.py test
```

### Built With
- Django and Django Rest Framework - The web framework used
- Vue js – Front end Javascript framework for SPAs
