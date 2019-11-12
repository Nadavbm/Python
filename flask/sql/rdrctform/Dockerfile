FROM python:3.7-alpine

RUN apk update && \
	apk add socat sqlite

RUN mkdir /app && \
	mkdir /install

WORKDIR /install
COPY requirements.txt /install
RUN pip install --no-cache-dir -r requirements.txt

ADD app/ /app

WORKDIR /app

RUN python initializedb.py

CMD ["python", "run.py"]
