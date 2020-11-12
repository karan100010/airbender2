web: gunicorn wsgi:app
worker: celery worker --app=base.app --loglevel=INFO
