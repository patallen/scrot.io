# Scrot.io
Take screenshots of the homepage of any website. Share them, tag them, organize them.

## Prep
1. Build phantomjs from source
1. Install postgresql and libpq-dev
1. Install virtualenvwrapper

## Set up database
1. Create database
1. Add user with only createdb premission
1. Give the user a password
1. Grant all privileges on database

## Set up Project
1. `$ pip install -r requirements.txt`
1. `$ ./manage.py migrate`
1. `$ ./manage.py createuser`
1. `$ ./manage.py runserver 0:8000`
