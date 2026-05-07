web: sh -c "python manage.py migrate --noinput && exec gunicorn PersonalWebsite.wsgi --bind 0.0.0.0:${PORT:-8000}"
