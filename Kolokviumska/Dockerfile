FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

RUN chmod +x /app/start.sh

ENTRYPOINT ["/bin/sh", "-c", "/app/start.sh"]

