# Template Django Project

- Docker
- PostgreSQL for dev and prod
- SQLite for testing
- pytest (don't add .vscode foder to .gitignore)
- API
- templates with tailwind CSS
- HTMX for rerendering only needed frontend components without a reload
- Django Allauth with Google login

## To install this project you can foollow this example:

```
git clone https://github.com/DenisBurimov/drf.git
cd drf
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## To fill your database with initial development data:

```
python manage.py fill_db
```

## For running Tailwind server with constant reload:

```
python manage.py tailwind start
```

## To see all routes and endpoints:

```
python manage.py routes
```
