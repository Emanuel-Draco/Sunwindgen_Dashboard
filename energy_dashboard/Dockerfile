ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3 py3-pip

WORKDIR /app

COPY app /app
COPY run.sh /run.sh

RUN pip3 install --no-cache-dir --break-system-packages -r /app/requirements.txt
RUN chmod +x /run.sh

ENV SECRET_KEY=change_me_later

CMD ["/run.sh"]
