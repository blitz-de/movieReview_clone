# Django: 
A webframework.You can use it to create dynamic websites. it is fast, well-secured, completly equiped. 

# Start a django project. Create a project called movie review, wit manage.py 
1. django-admin startproject moviereview
2. django manage.py makemigrations
3. django manage.py migrate
4. python manage.py runserver

------------------------

# Apps: 
are basically the part of the website. For example, we create app for account management, polls, or whatever component you fell like needs to have its own indivuality.
# Start first app
1. django-admin startapp <appName>
2. django-admin startapp main

# register app to settings.py
1. add the new app to the array of INSTALLED_APPS

# Run migrations again
1. python3 manage.py makemigrations
2. python3 manage.py migrate


-------------------------
# Django-File-structure:
moviereview> moviereview, main, manage.py db.sqlite3
* manage.py -> to start app or project
* settings.py -> configuration of the project, it's an engine like
* url.py -> defines the urls of the website
* wsgi.py -> during deployment it is needed
* admin.py -> 
* models.py -> database, where to create all the tables
* tests.py -> only needed, if i want to make tests
* views.py -> to interact with the database

-------------------------
# URls

we create urls for each app. 

------------------------
# Views

1. Create a view function with a 'request' parameter. 
2. Import this function in url.py
	a. use the . sign to import views and everything in it
	b. include the functions needed in the urlpatterns array, for example path('', views.home, name='home')

------------------------
# Models: 
To create databases

1. import models from django.db
# creating a table called Movie with specific instances having different properties. 
2. class Movie(models.Model): name = models.CharField(max_length=300) usw.
# to return the name in a string form
3. def __str(self): return self.name

----------------------------
admin.py : register the created tables in the models.py

# import all from models. 
1. from . import *
# register the table in admin.py
2. admin.site.register(Movie)

--> after these changes migrate the app. 

------
# Create Django Admin Panel
Inside of terminal

1. python3 manage.py createsuperuser

	a. Username: admin
	b. Emailaddress: whatever, etc.
	c. pass: 1234

2.  python manage.py runserver

	a. to access the new user. Just checkout localhost:8000/admin
	b. to access the tables. localhost:8000/ad,om/main/movie/
------
# Retrieve data from Database
* CRUD Principle - Create, Read, Update, Delete
* To Retrieve, just write the following line in views.py

	1. ```allMovies = Movie.objects.all()```
