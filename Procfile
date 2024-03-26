release: python manage.py migrate
web: gunicorn nomads_alchemy.wsgi:application
celery: celery -A nomads_alchemy worker --loglevel=INFO
celerybeat: celery -A nomads_alchemy beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
