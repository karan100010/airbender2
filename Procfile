web: gunicorn wsgi:app
worker: celery -A app.base:celery worker --loglevel=info
