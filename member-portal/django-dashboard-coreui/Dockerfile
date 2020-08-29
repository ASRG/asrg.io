FROM python:3.6


ENV FLASK_APP run.py


RUN mkdir -p /opt/code
COPY manage.py gunicorn-cfg.py requirements.txt .env /opt/code/
COPY app /opt/code/app/
COPY website /opt/code/website/
COPY authentication /opt/code/authentication/
COPY core /opt/code/core/
WORKDIR /opt/code
RUN ls

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations --no-imput"]
CMD ["python", "manage.py", "migrate --no-input"]
CMD ["python", "manage.py", "collectstatic --no-input"]

EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
