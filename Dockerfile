FROM python:3.10

WORKDIR /app

RUN pip install poetry==1.1.14

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY openapi.yaml .
COPY src src

ENV POSTGRES_HOST=drivacluster.ddns.net
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=cdp
ENV POSTGRES_PASSWORD=password_cdp_password
ENV POSTGRES_DBNAME=cdp

ENV ELASTIC_HOST=https://elastic.datadriva.com:443
ENV ELASTIC_USER=biga
ENV ELASTIC_PASSWORD=tBmWP6crnc9iqkU

CMD [ "poetry", "run", "python", "src/main.py" ]
