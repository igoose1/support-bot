FROM alpine:3.8

MAINTAINER Oskar Sharipov <oskarsh[at]riseup[dot]net>

RUN apk add --no-cache python3

WORKDIR /app
COPY . /app
RUN pip3 install -r /app/requirements.txt

CMD python3 /app/main.py
