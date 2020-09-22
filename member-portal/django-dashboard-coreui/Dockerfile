FROM python:3.6


ENV FLASK_APP run.py


RUN mkdir -p /opt/code
COPY manage.py gunicorn-cfg.py requirements.txt .env* docker-entrypoint.sh /opt/code/
RUN  chmod 777 /opt/code/docker-entrypoint.sh
COPY app /opt/code/app/
COPY website /opt/code/website/
COPY authentication /opt/code/authentication/
COPY core /opt/code/core/
WORKDIR /opt/code

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5005
