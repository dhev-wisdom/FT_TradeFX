FROM python:3.11.4
WORKDIR /app


RUN apt-get update

RUN pip install -r requirements.txt
RUN echo "CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': ['redis://redis:6379'],
        },
    }," >> settings.py

RUN echo "DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'TradeFX_',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            'host': os.environ.get('HOST'),
        }  
    }
}" >> settings.py
COPY . /app
CMD ["daphne", "-b", "0.0.0.0:8000", "tradeapp.asgi:application"]