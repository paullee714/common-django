# Django Common Template

# 실행방법

## develop
### run on server
```shell
poetry run python manage.py runserver --settings=config.settings.dev 
```
### db migrations
```shell
poetry run python manage.py makemigrations --settings=config.settings.dev
poetry run python manage.py migrate --settings=config.settings.dev
```

## prod
### run
```shell
poetry run python manage.py runserver --settings=config.settings.prod 
```
### db migrations
```shell
poetry run python manage.py makemigrations --settings=config.settings.prod
poetry run python manage.py migrate --settings=config.settings.prod
```