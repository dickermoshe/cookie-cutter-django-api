FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", ":80", "{{cookiecutter.project_slug}}.wsgi:application"] 