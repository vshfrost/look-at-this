FROM python:3.12-slim

WORKDIR /application

COPY app/ ./app
COPY .env ./.env
COPY database/ ./database
COPY requirements/ ./requirements
COPY env/app/start.sh ./app-start.sh

RUN chmod +x ./app-start.sh
RUN pip install --no-cache-dir -r ./requirements/base.txt

EXPOSE ${APP_PORT}

ENV PYTHONPATH=/application/app

ENTRYPOINT ["./app-start.sh"]
