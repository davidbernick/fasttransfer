#BROKER_URL = 'amqp://'
BROKER_URL = 'amqp://guest@localhost//'
#'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'America/New_York'
CELERY_ENABLE_UTC = True

from kombu import Exchange, Queue

CELERY_DEFAULT_QUEUE = 'celery'
CELERY_QUEUES = (
    Queue('celery', Exchange('celery'), routing_key='celery'),
    Queue('files', Exchange('files'), routing_key='files'),
)

#PYTHONPATH=$PYTHONPATH:/Users/dbernick/git/fasttransfer/src celery worker -A FastTransfer.tasks -c 1 -E -l info -Q celery
#PYTHONPATH=$PYTHONPATH:/Users/dbernick/git/fasttransfer/src celery worker -A FastTransfer.tasks -c 4 -E -l info -Q files
