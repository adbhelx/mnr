import os
import multiprocessing

# Gunicorn config variables
bind = "0.0.0.0:" + os.environ.get("PORT", "10000")
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
timeout = 60
preload_app = True
# The location of Gunicorn's temporary file
worker_tmp_dir = '/dev/shm'


# Hook for when the master process is started
def on_starting(server):
    # This is a good place to run setup tasks that only need to happen once
    # We will set the webhook here
    from majid.main import setup_webhook
    setup_webhook()

