FROM python:3.9

RUN mkdir /app/
WORKDIR /app/

COPY src /app/src/
COPY etc /app/etc/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN python3 -m venv .venv
COPY docker-entrypoint.sh /usr/bin/

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]


