FROM python:3.11.4
WORKDIR /app


RUN apt-get update && apt-get install -y build-essential

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

COPY static /app/static

RUN python manage.py collectstatic --noinput

RUN echo "* * * * * python3 manage.py tradeapp.simulate.simulate_profit_loss" >> crontab

RUN crontab crontab

CMD ["daphne", "-b", "0.0.0.0", "tradeFX.asgi:application"]