FROM ghcr.io/home-assistant/amd64-base-python:3.12

WORKDIR /app
COPY app /app
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]

