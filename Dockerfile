FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /channels_test
WORKDIR /channels_test
COPY . /channels_test/
RUN pip install -r requirements.txt
