FROM python:3.11
WORKDIR /app
RUN apt-get update && apt-get install -y librdkafka-dev build-essential
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]
