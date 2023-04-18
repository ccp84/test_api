# Project development

* Install django `pip install 'django<4'`
* Install rest `pip install djangorestframework`
* Start your project `django-admin startproject pelopals .`
* Create app `python manage.py startapp pelofondo`
* Add app to settings.py
* Create Procfile include `web: gunicorn pelopals.wsgi`
* Migrate (throughout) `python manage.py migrate`
* Create superuser `python manage.py createsuperuser`
* Add models - makemigrations - migrate - add to admin