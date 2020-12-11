# Welcome to the asrg.io github account.  

Join the discussion in our Slack channel: [Link](https://join.slack.com/t/asrg/shared_invite/enQtNTYzMjE5NDcyMzUyLWZmMzBhYTRmMzIzZDMyODA5NDkwZDc0Y2EwMDc5NjM2ODhlYWM5NjVlZjY3OWQyMGZhMDljNWI5ZDI1OWUzMDc)

## Contribution Guidelines

ASRG.io is constantly being developed to bring new benefits to the ASRG's membership around the world. As a non-profit, we need help. We believe that providing a platform for members to use will *fundamentally* impact vehicle safety by creating a place to share *knowledge*, facilitate *networking*, and foster *collaboration*.

ASRG.io is the main member portal that we are seeking to centralize our member's user experience around. It will be the single point of contact with all of our members and leads. In the same place, we imagine our regional/local leads and academic leads to *schedule* events and members to *view events/attend events*. We imagine a tab where members can access the "Automotive Security Intelligence Project (ASIP)", effectively allowing the member to get an update on the latest intelligence in the space. We imagine job postings by companies that our members can access. We imagine an education platform in the member portal that allows our members to learn about topics in automotive security.

To date, this portal has been developed by volunteers. Check out the latest release at https://asrg.io. If you want to participate in developing this platform to serve the industry and ultimately make vehicles more safe, reach out to us at hello@asrg.io (or message in github - really, just get in contact any way :) ).

We organize feature development in the *develop* branch. Big changes can be performed in a new branch from develop.

We frequently deploy by creating a pull request from develop to master, and pushing master to our web servers.

## Project Technical Background

Because we're all volunteers with limited time, we chose the path of least resistance to build this portal. Thus, we chose *Django* to build this web app. The core of the application was built on the Django+Gunicorn version of CoreUI. (https://github.com/app-generator/django-dashboard-coreui). They gave a nice template for standard use cases in a basic UI (i.e. handles authentication/authorization/roles well). They also gave us a nicely bundled database (Postgres) and proxy (nginx) all bundled neatly in a docker container that makes it easy to develop on AND deploy to our server.

Link to CoreUI: https://coreui.io/?ref=appseed

## Getting Started

You want to run this app locally in a nice, neat docker container (or just the django app to get rid of the docker complexity). Great! Here's how you would do that.

#Running in Docker

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/ASRG/asrg.io.git
$ cd asrg.io
$ touch .env
```

### The .env file
A hidden file used by Dockerfile and docker-compose, in order to enable environment variables
 while running/building with docker commands. This will not exist as it doesn't live in the git repo! You must create this env file yourself.
* Make sure this file is `.gitignored` but present in path: `~\asrg.io\.env`
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
# Modify this line if you want to add other ALLOWED_HOSTS
ALLOWED_HOSTS="localhost",  "127.0.0.1"
ASRG_APP_PORT=5005

# POSTGRES CONFIG
POSTGRES_USER=changeme
POSTGRES_PORT=5432
POSTGRES_DB=asrg
POSTGRES_PASSWORD=changeme_pass
PGDATA=/var/lib/postgresql/data/asrg/

# NGINX CONFIG
# Change this with the path to your certs
CERTS_PATH=./nginx
NGINX_HTTP_PORT=8080
NGINX_HTTPS_PORT=443
SERVER_NAME=localhost
DOLLAR=$
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
* For [admin](http://localhost:8080/admin)
  * To create admin credentials you need to  follow these steps:
  1) Enter the django container: `docker exec -it asrg-app /bin/bash`
  2) Tell django to create a new superuser.
  ```bash
  python manage.py createsuperuser
  ```
  3) log in to your superuser at /admin. Now, you can upgrade users through the admin page instead of in the container!



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

* `~\django_app\gunicorn-cfg.py`
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

#Running the Django app [TODO]

#Management
Tasks for feature development on this project are managed in Github Projects via sprints.
