FROM python:3.10

WORKDIR /app

RUN pip install poetry==1.1.14

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY openapi.yaml .
COPY src src

ENV POSTGRES_HOST=192.168.1.64
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DBNAME=postgres

ENV ELASTIC_HOST=http://192.168.1.64:9200
ENV ELASTIC_USER=elastic
ENV ELASTIC_PASSWORD=elastic

CMD [ "poetry", "run", "python", "src/main.py" ]
