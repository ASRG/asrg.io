FROM python:3.6
ENV FLASK_APP run.py

RUN apt-get update && apt-get install -y libgdal-dev g++ --no-install-recommends && apt-get clean -y
RUN mkdir -p /opt/code
WORKDIR /opt/code
COPY ./django_app/ /opt/code/

RUN  chmod 777 /opt/code/docker-entrypoint.sh
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5005
