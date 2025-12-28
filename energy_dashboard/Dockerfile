ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY app /app
COPY run.sh /run.sh
COPY static /app/static

RUN pip3 install --no-cache-dir --break-system-packages -r /app/requirements.txt
RUN chmod +x /run.sh

CMD ["/run.sh"]
