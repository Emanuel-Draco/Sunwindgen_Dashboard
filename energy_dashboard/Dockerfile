ARG BUILD_FROM
FROM $BUILD_FROM

WORKDIR /app
COPY app /app
COPY run.sh /run.sh

RUN chmod +x /run.sh

CMD ["/run.sh"]


