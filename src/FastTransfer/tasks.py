from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//')
celery.config_from_object('FastTransfer')

@celery.task
def add(x, y):
    return x + y