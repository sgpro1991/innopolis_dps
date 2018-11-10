#!/bin/bash

until python manage.py inspectdb >/dev/null 2>&1
do
  echo ">> waiting for database..."
  sleep 5
done

echo ">> database is up."

# apply database migrations
python manage.py migrate

# collect static files
python manage.py collectstatic --noinput

#python manage.py set_data
# start server
exec uwsgi --master --ini /conf/app.ini
#exec uwsgi --emperor /conf/
