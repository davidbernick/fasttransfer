from celery import Celery
import os
import ConfigParser
from .Job import crawlType

celery = Celery('tasks', 
                broker='amqp://guest@localhost//',
                backend='amqp://guest@localhost//')
celery.config_from_object('FastTransfer')

config = ConfigParser.ConfigParser()
try:
    config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
    broker = config.get('Celery', "broker")
    backend = config.get('Celery', "backend")
    celery = Celery('tasks', 
                    broker=broker,
                    backend=backend)
    celery.config_from_object('FastTransfer')

except Exception,e:
    raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))


@celery.task
def add(x, y):
    return x + y

@celery.task
def newJob(job):
    if job.crawlTypeSelected==crawlType["stash"]:
        job.stashCrawl()
    elif job.crawlTypeSelected==crawlType["files"]:
        job.filesCrawl()
    if job.crawlTypeSelected==crawlType["dir"]:
        job.dirCrawl()
    return job.toJson()

@celery.task
def processFile(fc_container):
    return 0
