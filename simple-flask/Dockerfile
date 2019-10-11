FROM python:3.7-alpine

RUN mkdir /install && \
    mkdir /simple-flask

COPY requirements.txt /install
WORKDIR /install
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ /simple-flask
WORKDIR /simple-flask

CMD ["python", "app.py"]


