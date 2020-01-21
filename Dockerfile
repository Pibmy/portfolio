FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /portfolio
WORKDIR /portfolio

COPY requirements.txt /portfolio/
RUN pip install -r portfolio

COPY . /portfolio/