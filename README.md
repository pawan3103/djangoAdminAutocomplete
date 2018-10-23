#Autocomplete for Foreignkeys in Django Admin#

In this Article I will explain you how we can add autocomplete for Foreignkeys in Django Admin Panel. Sometimes we might come across case where we need to map entry for existing records or create records from Admin panel which has foreignkey relationships now if there are some hundreds or thousands of records present in Foreignkey model than it becomes difficult to map it, so to overcome the problem we have added autosearch filter in Foreignkeys.

#Project Setup#
 
- After cloning the repo, create Virtual Environment for Python2.7/Python3.6, it will work for both.
- Let's create it for python2.7.

- `virtualenv env` use following command to create environment.
- Use `source env/bin/activate` to activate environment.
- Install all the dependencies, from requirements.txt file `pip install -r requirements.txt`
- `python manage.py migrate` to migrate the db.
- `python manage.py createsuperuser` to create superuser.
- `python manage.py runserver` and login `localhost:8000/admin`.
 




