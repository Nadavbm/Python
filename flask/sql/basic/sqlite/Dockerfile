FROM python:3.7-alpine

RUN apk update \
    && apk add sqlite \
    && apk add socat

RUN mkdir /install && \
    mkdir /app

COPY requirements.txt /install
WORKDIR /install
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ /app
WORKDIR /app

RUN sqlite3 users.db

CMD ["python", "wsgi.py"]


