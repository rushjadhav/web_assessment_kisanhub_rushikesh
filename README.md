Weather Data Analyzer
=====================

Django project to retrieve, store and present UK weather data.

Setup
---------

* Clone repo --> `git clone https://github.com/rushjadhav/web_assessment_kisanhub_rushikesh.git`
* `cd web_assessment_kisanhub_rushikesh.git`
* Create virtual environment --> `virtualenv venv`
* Activate Virtual environment --> `source venv/actiavte`
* Install requirements --> `pip install -r docs/requirements.txt`
* `cd weather_data_analyzer` 
* Load initial data --> `python manage.py loaddata initial_data.json`
* Populate database with weather data --> `python manage.py populate_weather_data --all`
* Run Test cases --> `python manage.py test`
* Run server `python manage.py runserver 127.0.0.1:8000`
* Visit site `127.0.0.1:8000`
