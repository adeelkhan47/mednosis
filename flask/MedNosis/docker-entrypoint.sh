#!/bin/sh

set -e
cd /app/
. .venv/bin/activate
python3 -m pip install -r etc/requirements.txt

cd src

# No flask migrate, uses alembic
# while ! flask db upgrade
# do
#      echo "Retry..."
#      sleep 1
# done

exec gunicorn --bind 0.0.0.0:8000 --timeout 432000 --forwarded-allow-ips='*' wsgi:app
