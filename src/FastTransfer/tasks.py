from celery import Celery
import Job
from Job import crawlType

celery = Celery('tasks', broker='amqp://guest@localhost//')
celery.config_from_object('FastTransfer')

@celery.task
def add(x, y):
    return x + y

@celery.task
def newJob(job):
    if job.crawlTypeSelected==crawlType["stash"]:
        stashCrawl(job)
    elif job.crawlTypeSelected==crawlType["files"]:
        filesCrawl(job)
    if job.crawlTypeSelected==crawlType["dir"]:
        dirCrawl(job)
        
    return job.toJson()