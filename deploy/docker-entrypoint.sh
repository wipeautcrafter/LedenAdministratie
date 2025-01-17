#!/bin/sh

# Activate python3 venv
source /srv/venv/bin/activate

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

# Update font cache
/usr/bin/fc-cache

# Start nginx
nginx

# Start jobs in a loop
sh /jobs.sh &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn LedenAdministratie.wsgi:application \
    --name LedenAdministratie \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"
