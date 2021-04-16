FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn"  , "-b", "0.0.0.0:8080", "app:server"]