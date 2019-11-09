FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r /code/requirements.txt
COPY dev-requirements.txt /code/
RUN pip install -r /code/dev-requirements.txt
ADD . /code/ipmap
WORKDIR /code/ipmap/ipmap