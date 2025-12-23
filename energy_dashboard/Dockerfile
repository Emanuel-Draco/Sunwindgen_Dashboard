ARG BUILD_FROM
FROM $BUILD_FROM

# Python + wymagane biblioteki (TYLKO APK)
RUN apk add --no-cache \
    python3 \
    py3-fastapi \
    py3-uvicorn \
    py3-jose

WORKDIR /app

COPY app /app
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]
