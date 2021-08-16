FROM python:3-slim

ENV ROOT=/app
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

WORKDIR $ROOT

RUN python -m venv /venv

COPY --chown=65534:65534 . $ROOT

RUN pip install -r requirements.txt \
    && python manage.py migrate \
    && chown -R 65534:65534 $ROOT /venv

USER nobody

EXPOSE 8000

ENTRYPOINT ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
