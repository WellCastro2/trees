FROM python:3.8.5

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev
RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
