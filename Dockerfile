FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "-c", "./entrypoint.sh"]