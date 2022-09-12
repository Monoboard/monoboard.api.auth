FROM python:3.9.13

RUN mkdir /src
COPY requirements.txt requirements-dev.txt src /src/

ENV TZ=Europe/Kiyv
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --upgrade pip && \
    pip install -r /src/requirements.txt && \
    pip install -r /src/requirements-dev.txt

WORKDIR /src
