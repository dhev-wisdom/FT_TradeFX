FROM python:3.11.4
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN pip install --upgrade pip
COPY .requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["daphne", "tradeapp.asgi"]