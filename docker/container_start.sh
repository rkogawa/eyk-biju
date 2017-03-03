#!/bin/sh
cd /var/projects/eykbiju && python3 manage.py migrate --noinput
supervisord -n -c /etc/supervisor/supervisord.conf