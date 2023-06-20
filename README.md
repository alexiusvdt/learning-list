
# Learning Log

#### Storing topics & associated entries

#### By Alex Johnson

## Technologies Used

* python
* Django

## Description/user stories
- Learning Log will allow users to log the topics they're interested in and make journal entries as they learn about each topic.
- The home page will describe the site and invite users to register or log in.
- Once logged in, a user can create a new topic, add new entries, and read/edit existing entries.

## Setup/Installation Requirements
<!-- verify these steps are correct -->
install necessary packages:

* create the virtual environment: `python -m venv ll_env`

*Activate the environment

  for macOS: `source ll_env/bin/activate`

  for Win: `cd` into `ll_env` and run `the command .\Scripts\activate

  your terminal should show: `((ll_env)) C:\...`

* run `pip install django' (since we're in a virtual env no need for the --user flag, but django will only be active when this env is)

* run `python manage.py migrate` to apply migrations

* verify project has been set up correctly by running `python manage.py runserver` (default should be localhost:8000)

* run `python manage.py createsuperuser`(note that email is stored as hash) to create an admin account. Obey the wizard.

* open to localhost:8000/admin for admin-level access (creating topics & entries)

## Known Bugs
* it's not very pretty

## Additional Thanks
Eric Matthes for the helpful crash course & creative spark!

## Future implementations


## License
MIT License

Copyright (c) 2023 Alex Johnson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS 
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

=============
Study notes:

*before hosting:
remove debug mode
change secret key (both in learning_log/settings.py)


templating:
run `django-admin startproject project_name .` (DO NOT forget the dot)

this creates a bunch of template stuff, the named dir containing 4 files:
- settings: controlling how Django interacts with the system & project
- urls.py tells Django which pages to build in response to browser requests
- wsgi.py helps serve the files it creates (web server gateway interface)

run `python manage.py migrate` to apply the migration (SQLite)

verify project has been set up correctly by running `python manage.py runserver` (default should be localhost:8000)

`python manage.py startapp learning_logs` tells Django to create infrastructure to build an app (a project is built of many apps)

When modifying the data the project manages, take these 3 steps:

- modify models.py 

- call `python manage.py makemigrations learning_log`: makemigrations tells Django to ffigure out how to modify the db so it can store the associated data with any new models.

- call `python manage.py migrate` to actually apply it

======================
creating users
`python manage.py createsuperuser`(note that email is stored as hash)

obey the wizard

=======================
in the (ll_env) run `python manage.py shell` to launch the Django shell

`from learning_logs.models import Topic`

`Topic.objects.all()` will return a `<QuerySet [<Topic: topic1>, etc]>

this can be looped like a list:

```
topics = Topic.objects.all()
for topic in topics:
  print(topic.id, topic)
```

we can look at associated attributes:

```
t = Topic.objects.get(id=1)
t.text
t.date_added
```

Even grab all associated entries! (this will return the truncated version)
```
t.entry_set.all()
```

======
general step: registering views/templates
-create the url in the learning_log/urls.py folder (this is for setting up superpatterns like  /admin, '', etc i think)
-create the urlpattern in the learning_logs/urls.py folder (specific /topic /details, etc)
-create the view