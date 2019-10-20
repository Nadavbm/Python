FROM python:3.7-alpine

RUN mkdir /install && \
    mkdir /flask-html

COPY requirements.txt /install
WORKDIR /install
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ /flask-html
WORKDIR /flask-html

CMD ["python", "app.py"]


