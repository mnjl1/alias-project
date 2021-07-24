# Alias-project (test task)

Set up a basic Django project with a single alias app, allowing to find
other objects from a common entry point.

## how to launch with docker

...sh
docker-compose up -d --build
...

## if no docker

...sh
source env/bin/activate
pip install -r requirements.txt
python manage.py test
...

## how to test

...sh
python manage.py test
...
