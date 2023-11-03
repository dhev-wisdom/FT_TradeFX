FROM python:3.11.4
WORKDIR /app


RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "CHANNEL_LAYERS = {" >> settings.py
RUN echo "    'BACKEND': 'channels_redis.core.RedisChannelLayer'," >> settings.py
RUN echo "    'CONFIG': {" >> settings.py
RUN echo "        'hosts': ['redis://redis:6379']," >> settings.py
RUN echo "    }," >> settings.py

COPY . /app
CMD ["daphne", "-b", "0.0.0.0:8000", "tradeFX.asgi:application"]