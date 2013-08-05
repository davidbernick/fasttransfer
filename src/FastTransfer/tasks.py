from celery import Celery
import os
import ConfigParser
import Job
import time
from FastTransfer import celeryconfig

celery = Celery('tasks' )
celery.config_from_object(celeryconfig)
print celery


@celery.task
def add(x, y):
    return x + y

@celery.task
def newJob(job):
    if job.crawlTypeSelected==Job.crawlType["stash"]:
        job.stashCrawl()
    elif job.crawlTypeSelected==Job.crawlType["files"]:
        job.filesCrawl()
    if job.crawlTypeSelected==Job.crawlType["dir"]:
        job.dirCrawl()
    return job.toJson()

@celery.task
def processFileContainer(fc_container):
    #tags for each file: mtime, atime, owner, group, dir, parentdir, filename

    #for each file
    #see if file already exists
    #see if it's datestamp is different
    #if different, upload
    return 0
