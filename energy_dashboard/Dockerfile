ARG BUILD_FROM=ghcr.io/home-assistant/amd64-python:3.12
FROM $BUILD_FROM

WORKDIR /app

COPY app /app
COPY run.sh /run.sh

RUN pip install --no-cache-dir fastapi uvicorn python-jose

RUN chmod +x /run.sh

CMD ["/run.sh"]
