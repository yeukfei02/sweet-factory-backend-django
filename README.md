# sweet-factory-backend-django

sweet-factory-backend-django

documentation: <https://documenter.getpostman.com/view/3827865/2sAYBbepF4>

api url: <http://localhost:8000>

admin portal url: <http://localhost:8000/admin>

## Requirement

- install python (v3.12)

## Testing and run

```zsh
// install dependencies
$ pip install -r requirements.txt

// run api in local
$ python manage.py runserver

// create migration for module
$ python manage.py makemigrations <module-name>

// db migration
$ python manage.py migrate

// db rollback
$ python manage.py <module-name> <migration-name>

// show db migration
$ python manage.py showmigrations

// db reset
$ python manage.py reset_db

// list routes
$ python manage.py show_urls
```
