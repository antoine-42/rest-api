# rest-api

## Dev

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open your browser at http://0.0.0.0:8000

## Docker

```shell
docker build -t game_api:latest .
docker-compose up
```

Open your browser at http://0.0.0.0:8008

## Travail réalisé

Sujet principal, avec Django-Rest-Framework, une BDD Sqlite, et déploiement sur Docker.

Dashboard:
- /games/?ordering=ratings
- /games/?ordering=release_date
- /platforms/
