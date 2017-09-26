# python image using Debian Jessie
FROM python:latest
ENV PYTHONUNBUFFERED 1
COPY ./src /opt/office-manager
COPY ./development.env /opt/office-manager/.env
COPY requirements.txt /opt/office-manager/
WORKDIR /opt/office-manager
RUN pip3 install pip
RUN pip3 install -r ./requirements.txt
RUN adduser --disabled-password --gecos '' office_user
