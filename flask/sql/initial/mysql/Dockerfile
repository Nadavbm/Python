FROM python:3.7-alpine

RUN apk add mysql-client

RUN mkdir /install && \
    mkdir /app

COPY requirements.txt /install
WORKDIR /install
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ /app
WORKDIR /app

CMD ["python", "app.py"]


