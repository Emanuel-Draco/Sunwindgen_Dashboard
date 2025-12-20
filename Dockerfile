ARG BUILD_FROM
FROM $BUILD_FROM

# Python z apk (bez pip install!)
RUN apk add --no-cache python3

WORKDIR /app

COPY app .
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
