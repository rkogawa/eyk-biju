#!/bin/sh
cd /var/projects/eykbiju && python manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf