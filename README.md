# Epimedictor

Given a medical symptom, list down the possible medical conditions/diagnosis and for any given diagnosis suggest various treatments.

## Getting Started

1. Clone this repository: `git clone git@github.com:gothinkster/productionready-django-api.git`.
2. Create a database and user using data in section `DATABASES` in file `epimedictor/settings.py`.
3. Migrate the Database :
```
python manage.py makemigrations
python manage.py migrate
```
4. Run server: `python manage.py runserver`.
5. Access using `http://127.0.0.1:8000/` in a web browser.


### Features

1. API 1 : To fetch the symptoms
○ Apimedic​ ’s APIs is used to get the symptoms
```
http://127.0.0.1:8000/symptoms/
```
2. API 2: For a given symptom , give the medical conditions
```
Example : http://127.0.0.1:8000/conditions/?symptoms=[9]&gender=male&year_of_birth=1982
```
3. API 3: For a given medical condition/diagnosis
○ Provides the treatment
○ Treatment is obtained by scraping the web
○ Any subsequent call for the disease fetches the data from the database itself
```
Example : http://127.0.0.1:8000/treatment/?issue=104&issue_condition=Cephalalgia
```
### Requirements

Specified in requirement.txt file.

## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [MySQL](https://dev.mysql.com/doc/) - Database




