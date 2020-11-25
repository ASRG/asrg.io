# [Django Dashboard CoreUI](https://appseed.us/admin-dashboards/django-dashboard-coreui)

> **Open-Source Admin Dashboard** coded in **Flask Framework** by **AppSeed** [Web App Generator](https://appseed.us/app-generator) - features:

- UI Kit: **[CoreUI Dashboard](https://coreui.io/?ref=appseed)** (Free version) provided by **CoreUI**
- UI-Ready app, SQLite Database, Django Native ORM
- Modular design, clean code-base
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx
- **MIT License**
- Free support via **Github** 
- Paid Support **24/7 LIVE Support** via [Discord](https://discord.gg/fZC6hup)

> Links

- [Django Dashboard CoreUI](https://appseed.us/admin-dashboards/django-dashboard-coreui) - Product page
- [Django Dashboard CoreUI](https://django-dashboard-coreui.appseed.us/) - LIVE Demo
- [Django Dashboard CoreUI](https://docs.appseed.us/admin-dashboards/django-dashboard-coreui/) - Docs
- More [Django Admin Dashboards](https://appseed.us/admin-dashboards/django) - index hosted by **AppSeed**
- [Free Admin Dashboards](https://appseed.us/admin-dashboards/open-source) - index hosted by **AppSeed**

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Django DattaAble Dark PRO](https://appseed.us/admin-dashboards/django-dashboard-dattaable-dark-pro) | [Django Dashboard Black PRO](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [Django StarAdmin Dark PRO](https://appseed.us/admin-dashboards/django-dashboard-staradmin-black-pro) |
| --- | --- | --- |
| [![Django DattaAble Dark PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-dattaable-dark-pro/master/media/django-dashboard-dattaable-dark-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-dattaable-dark-pro) | [![Django Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-black-pro/master/media/django-dashboard-black-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [![Django StarAdmin Dark PRO](https://raw.githubusercontent.com/app-generator/django-dashboard-staradmin-black-pro/master/media/django-dashboard-staradmin-black-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-staradmin-black-pro)

<br />
<br />

![Django Dashboard CoreUI - Open-Source Web App.](https://raw.githubusercontent.com/app-generator/static/master/products/django-dashboard-coreui-screen.png)

<br />

## How to use it

```bash
# 1. Get the code
$ git clone https://github.com/ASRG/asrg.io.git
$ cd member-portal/django-dashboard-coreui/

# [Unix] 2. Virtualenv modules installation
$ virtualenv env
$ source env/bin/activate

# [Windows] 2. Virtualenv installation (Windows): python -m pip install --user virtualenv
python -m virtualenv env
.\env\Scripts\activate

# 3. Install modules - SQLite Storage
$ pip3 install -r requirements.txt

# 4. Create tables
$ python manage.py makemigrations && python manage.py migrate

# 5. Start the application (development mode) default port 8000
$ python manage.py runserver

# 6. To use PostgreSQL add this line to ~/asrg.io/member-portal/django-dashboard-coreui/.env
DATABASE_URL=postgres://changeme:changeme_pass@asrg-postgres:5432/asrg

# 7. (OPTIONAL) Start the app - custom port
python manage.py runserver 0.0.0.0:<your_port>

# 8. Access the web app in browser:
http://127.0.0.1:8000/
```

<br/>

## Deployment
The app is provided with a basic configuration to be executed in:
* [Heroku](https://heroku.com/)
* [Docker](https://www.docker.com/)
* [Django-CSP](https://github.com/mozilla/django-csp)
* [Gunicorn](https://gunicorn.org/)
* [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)


### Docker execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/ASRG/asrg.io.git
$ cd member-portal/django-dashboard-coreui
$ touch .env
```

### The .env file
A hidden file used by Dockerfile and docker-compose, in order to enable environment variables
 while running/building with docker commands.
* Make sure this file is `.gitignored` but present in path: `~\asrg.io\member-portal\django
-dashboard-coreui\django_app\.env`
* We need to specify Django to connect using this specific DB. By default, it will use sqlite if
 not declared. 
* If you wish to change the ports for NGINX you can change them in this file
* If you want to test with a local https certificate you can add the path to the certificates on
 the below config file.
  * Uncomment the line from `docker-compose.yml` with this path is also necessary, as well as
   uncommenting the lines from the nginx `config(./nginx/asrg.conf)`


``` bash
# DJANGO CONFIG 
DEBUG=True  # Set to false in PROD
DATABASE_URL=postgres://changeme:changeme_pass@asrg-postgres:5432/asrg
ALLOWED_HOSTS="localhost,  127.0.0.1"  # Modify this line if you want to add other ALLOWED_HOSTS
ASRG_APP_PORT=5005

# POSTGRES CONFIG
POSTGRES_USER=changeme
POSTGRES_PORT=5432
POSTGRES_DB=asrg
POSTGRES_PASSWORD=changeme_pass
PGDATA=/var/lib/postgresql/data/asrg/

# NGINX CONFIG
CERTS_PATH="./nginx"  # Change this with the path to your certs
NGINX_HTTP_PORT=8080
NGINX_HTTPS_PORT=443
SERVER_NAME=localhost
DOLLAR='$'
```
<br/>

> Pull image and start the app in docker-compose

```bash
# [Unix] To get rid of the containers that were renamed
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d --remove-orphans

# [Windows] To get rid of the containers that were renamed
docker-compose pull && docker-compose build && docker-compose up -d --remove-orphans
```

Visit [http://localhost:8080](http://localhost:8080) in your browser. The app should be up & running.
* For [login](http://localhost:8080/login/)

> Stop and remove the app with docker-compose

```bash
# [Unix]
$ sudo docker-compose stop && sudo docker-compose rm -f 

# [Windows]
docker-compose stop && docker-compose rm -f
```

> Build (update) the whole app (db, ui, etc.) with docker-compose

```bash
# [Unix] To get rid of the containers that were renamed
$ sudo docker-compose stop && sudo docker-compose build && sudo docker-compose up -d --remove-orphans

# [Windows] To get rid of the containers that were renamed
docker-compose stop && docker-compose build && docker-compose up -d --remove-orphans
```

> Build (update) specific container (db, ui, etc.) with docker-compose

The docker container for asrg-app is using a volume as mount binding point between the host files
 and the running docker container.

It also exists an option for gunicorn to reload every time it detects a change, so we don't have
 to restart the Docker container each time changes are done. This is only when DEBUG is set to
  True *(DO NOT run --reload for gunicorn in production)*.

* `~\member-portal\django-dashboard-coreui\django_app\gunicorn-cfg.py`
```python
if DEBUG:
    reload = True
```

If a rebuild stills required after some changes. You can run the next commands to update an
 specific container:

```bash
# [Unix] Stop and re build only the dashboard-ui for updates: asrg-app
$ sudo docker-compose stop asrg-app && sudo docker-compose rm -f asrg-app &&\
sudo docker-compose pull asrg-app && sudo docker-compose build asrg-app &&\
sudo docker-compose up -d --remove-orphans asrg-app

# [Windows] Stop and re build only the dashboard-ui for updates: asrg-app
docker-compose stop asrg-app && docker-compose rm -f asrg-app && docker-compose pull asrg-app && docker-compose build asrg-app && docker-compose up -d --remove-orphans asrg-app
```

<br/>

### Django-csp
---

[django-csp](https://django-csp.readthedocs.io/en/latest/) 'Django Content Security Policy'.

> Install using pip
```bash
$ pip install django-csp
```

<br/>

### Gunicorn
---

[Gunicorn](https://gunicorn.org/) 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip
```bash
$ pip install gunicorn
```

> Start the app using gunicorn binary
```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit [http://localhost:8001](http://localhost:8001) in your browser. The app should be up & running.

<br/>

### Waitress
---
[Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip
```bash
$ pip install waitress
```

> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)
```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit [http://localhost:8001](http://localhost:8001) in your browser. The app should be up & running.

<br/>

### Automatic migration of data
---

The database gets populated with the chapters that already exist before the creation of this django app, further chapters need to be added from the Admin interface.
If you want the events as well, there is a migration already created for this: `/member-portal/django-dashboard-coreui/django_app/events/migrations/0003_populate_initial_data.py`, in order for this to work you need to add the file `asrg_events.csv` to the following path:
`/member-portal/django-dashboard-coreui/django_app/events/migrations/`. The `asrg_events.csv` file has the following header:
```
ASRG,Host,Event,Check,Presenter,Organization,Type,Status,A,,Location,Start,End
```

<br/>

## Troubleshooting
### django.db.utils.OperationalError: could not translate host name "postgres" to address: Unknown host
> **Solution:** The issue was fixed, after latest changes update.


# Recreating CONTAINERID_asrg-postgres ... error
## ERROR: for CONTAINERID_asrg-postgres  Cannot create container for service asrg-db: Duplicate mount point: /var/lib/postgresql/data
### ERROR: for asrg-db  Cannot create container for service asrg-db: Duplicate mount point: /var/lib/postgresql/data
> **Solution:** This issue is related to older docker volumes (mount points for db), not being
> properly removed from older builds. To fix this issue we need to:
```bash
# 1. Check all containers for Exited, Stopped, etc related to *asrg*
$ docker container ps -a
# 2. Stop all these specific containers related to the db (use ID or name)
$ docker container stop CONTAINERID_asrg-postgres asrg-nginx asrg-app
# 3. Remove failing container due to old version
$ docker container rm -f CONTAINERID_asrg-postgres asrg-nginx asrg-app
# 4. Check docker volumes for old versions
$ docker volume ls
# 5. Remove old docker volumes
$ docker volume rm django-dashboard-coreui_db_data
# 6. Check docker networks for old versions
$ docker network ls
# 7. Remove old docker networks
$ docker volume rm django-dashboard-coreui_db_network django-dashboard-coreui_web_network
# 8. Clean for space (<none> images)
$ docker image prune
# 9. Finally, pull, build and run the dashboard (clean/fresh)
$ docker-compose pull && docker-compose build && docker-compose up -d --remove-orphans
# 10. Check all containers running then go to the site:
http://localhost:8080/login/
```

<br/>

## Credits & Links

### [Django Admin Dashboards](https://appseed.us/admin-dashboards/django)

Index with UI-ready **admin dashboards** generated by the AppSeed platform in [Django Framework](https://www.djangoproject.com/).
Start fast your next Django project by using functional admin dashboards enhanced with Database, ORM, authentication flow, helpers and deployment scripts.

### What is [Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.

### [What is a dashboard](https://en.wikipedia.org/wiki/Dashboard_(business))

A dashboard is a set of pages that are easy to read and offer information to the user in real-time regarding his business. A dashboard usually consists of graphical representations of the current status and trends within an organization. Having a well-designed dashboard will give you the possibility to act and make informed decisions based on the data that your business provides - *definition provided by [Creative-Tim - Free Dashboard Templates](https://www.creative-tim.com/blog/web-design/free-dashboard-templates/?ref=appseed)*.

### [CoreUI Dashboard](https://coreui.io/?ref=appseed)

**[CoreUI Dashboard](https://coreui.io/?ref=appseed)** admin dashboard delivers a bunch of responsive, customizable, and reusable components you need to create modern, beautiful, responsive apps. CoreUI makes app development lightning-fast - provided by **CoreUI**.

<br />

---

**[Django Dashboard CoreUI](https://appseed.us/admin-dashboards/django-dashboard-coreui)** - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
