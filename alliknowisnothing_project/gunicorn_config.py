
# start the app with gunicorn and this config from the project dir with:
# gunicorn -c gunicorn_config.py alliknowisnothing.wsgi:application

from multiprocessing import cpu_count

bind = '127.0.0.1:8000'
workers = cpu_count() * 2 + 1

daemon = True
