# Scrot.io
Take screenshots of the homepage of any website. Share them, tag them, organize them.

## Prep
1. Build phantomjs from source
1. Install postgresql and libpq-dev
1. Install virtualenvwrapper
1. install npm

## Set Up Assets
1. `$ npm install -g gulp`
1. `$ npm install -g bower`
1. `$ npm install`
1. `$ bower install`
1. `$ gulp sass:watch`

## Set up database
1. Create postgres database
1. Add user with only createdb premission
1. Give the user a password
1. Grant all privileges on database

## Set up Project
1. `$ pip install -r requirements.txt`
1. `$ ./manage.py migrate`
1. `$ ./manage.py createuser`
1. `$ ./manage.py runserver 0:8000`

## TODO:
- [ ] Snapshot Views
- [ ] Snapshot Likes
- [ ] AJAX take screenshot
- [ ] Better user registration
- [ ] Email notifications
- [ ] Activity Stream
- [ ] Snapshot error handling and timeout
- [ ] Download / Copy palette
- [ ] Website information (crawl, whois, metadata)
- [ ] Take Snapshot from website_detail
- [ ] Add to collection button/dropdown
- [ ] Collection detail page
- [ ] Website snapshot count
- [x] Add sticky footer
- [x] AJAX CSRF
- [x] Collection Model
- [x] Allow one snapshot per day
- [x] Watch Lists
- [x] Registration
