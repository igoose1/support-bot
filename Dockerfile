FROM alpine:3.8

MAINTAINER Oskar Sharipov <oskar.sharipov@tuta.io>

RUN apk add --no-cache \
    python3 \
    python3-dev

WORKDIR /app
COPY . /app
RUN pip3 install -r /app/requirements.txt

CMD python3 /app/main.py
