FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# TODO - replace this with gunicorn for production 
CMD [ "python", "app.py" ]