*before hosting:
remove debug mode
change secret key (both in learning_log/settings.py)


User Stories/Spec
- Learning Log will allow users to log the topics they're interested in and make journal entries as they learn about each topic.
- The home page will describe the site and invite users to register or log in.
- Once logged in, a user can create a new topic, add new entries, and read/edit existing entries.

create the virtual environment: `python -m venv ll_env`

Activate the environment

for macOS: `source ll_env/bin/activate`

for Win: `cd` into `ll_env` and run `the command .\Scripts\activate

your terminal should show:
((ll_env)) C:\users...etc

run `pip install django' (since we're in a virtual env no need for the --user flag, but django will only be active when this env is)

run `django-admin startproject project_name .` (DO NOT forget the dot)

this creates a bunch of template stuff, the named dir containing 4 files:
- settings: controllign how Django interacts with the system & project
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

