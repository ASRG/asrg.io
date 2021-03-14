
Great! You've read the README and you understand what the ASRG is and why we're developing this member portal.
- [Running in docker](#running-in-docker)
- [Setup .env file](#the-env-file)
- [Developing a Feature or a Change](#developing-a-feature-or-a-change)
- [Create local users for testing](#create-local-users-for-testing)
- [Code Style Guidelines](#code-style-guidelines)
## Getting Started

Join the discussion in our Slack channel: [Link](https://join.slack.com/t/asrg/shared_invite/enQtNTYzMjE5NDcyMzUyLWZmMzBhYTRmMzIzZDMyODA5NDkwZDc0Y2EwMDc5NjM2ODhlYWM5NjVlZjY3OWQyMGZhMDljNWI5ZDI1OWUzMDc)

You want to run this app locally in a nice, neat docker container (or just the django app to get rid of the docker complexity). Great! Here's how you would do that.

## Running in Docker

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

Great! You got your local member portal working. Now, let's go through how to make contribute changes to the member portal.

## Code Pipeline

Develop code in your local branch, then issue a pull request to have that branch merged into develop. Once it's in develop and demonstrated that the application is functional, develop will be periodically merged into master, which goes to the server.

### Developing a Feature or a Change.

1. Create a new branch that's named somewhat reasonably as it relates to the feature or change you're working on.
```
git checkout -b new-branch
```

2. Make your changes to that branch.
  -If you're adding a new functionality, create a new app with `python manage.py startapp name_of_the_app`
  -add it's requirements to YOURAPP/requirements.txt (make sure to include versions for the dependencies)
  -update `/django_app/asrg/requirements.txt` with `-r YOURAPP/requirements.txt`

3. Issue a pull request to have approved so that your branch can be merged into the develop branch.
## Create local users for testing
If you are running with docker run the following command to create local users:
```bash
 docker exec asrg-app python manage.py create_test_users --force
 ```
 If you are running locally without docker you can just run the following command inside the folder `django_app`
 ```bash
  python manage.py create_test_users
```
## Code Style Guidelines
1. We are using [Black](https://github.com/psf/black) to automatically format the code.
    - If you want to install black on your IDE you can find integrations [here](https://black.readthedocs.io/en/stable/editor_integration.html)
    - Run `pre-commit install` (it runs black, flake8 and checkf for missing migrations)
 
