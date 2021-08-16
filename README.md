# rest-api

## Dev

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open your browser at http://127.0.0.1:8000

## Docker

```shell
docker build -t game_api:latest .
docker-compose up
```

Open your browser at http://0.0.0.1:8008
