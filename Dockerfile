FROM python:3.5
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /apiDamificados
COPY apiDamificados /apiDamificados
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN pyhon manage.py collectstatic
CMD gunicorn --bind 0.0.0.0:8000 apiDamificados.wsgi:application
