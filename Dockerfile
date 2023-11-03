FROM python:3.11.4
WORKDIR /app


RUN apt-get update

RUN pip install -r requirements.txt

RUN echo "CHANNEL_LAYERS = {" >> settings.py
RUN echo "    'BACKEND': 'channels_redis.core.RedisChannelLayer'," >> settings.py
RUN echo "    'CONFIG': {" >> settings.py
RUN echo "        'hosts': ['redis://redis:6379']," >> settings.py
RUN echo "    }," >> settings.py

COPY . /app
CMD ["daphne", "-b", "0.0.0.0:8000", "tradeapp.asgi:application"]