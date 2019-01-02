FROM alpine:3.8

ENV PYTHONUNBUFFERED 1

COPY ./src /opt/office-manager
COPY ./.env /opt/office-manager/.env
COPY requirements.txt /opt/office-manager/

RUN apk --update add \
    gcc \
    jpeg-dev \
    libffi-dev \
    libressl-dev \
    make \
    musl-dev \
    postgresql-dev \
    # Python 3.6.6 is used
    python3 \
    python3-dev \
    zlib-dev \
 && adduser --disabled-password --gecos '' office_user \
 && cd /opt/office-manager \
 && pip3 install --upgrade pip \
 && pip3 install -r ./requirements.txt \
 && apk del \
    gcc \
    make \
    musl-dev \
    python-dev \
 && rm -rf /var/cache/apk/*

WORKDIR /opt/office-manager
