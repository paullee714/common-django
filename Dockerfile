FROM python:3.10.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install poetry


COPY pyproject.toml poetry.lock /code/
COPY . /code/

RUN poetry install --no-root
ENV DJANGO_CONFIG=prod
#RUN poetry run python manage.py crontab add
EXPOSE 8000
#CMD ["poetry","run","python", "manage.py","runserver", "--settings=config.settings.prod","0.0.0.0:8000"]
CMD ["poetry", "run", "gunicorn", "config.asgi:application", "-w", "4", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]