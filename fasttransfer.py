import sys, getopt,csv,os
#import hipchat.api
from os.path import expanduser
#from boto.s3.connection import S3Connection
import time
import uuid

from FastTransfer.Job import crawlType,Job
from FastTransfer.tasks import newJob,processFile
from FastTransfer.Log import Log

aws_key=""
aws_secret=""
DRYRUN=False

logger = Log.getLog()

def startCrawl(crawlPath=None,crawlKey="stash"):
    global aws_key
    global aws_secret
    global DRYRUN
    global logger

    if crawlKey=="" or crawlKey==None:
        crawlKey="stash"
    
    job = Job(crawlPath=crawlPath,
              crawlKey=crawlKey,
              aws_key=aws_key,
              aws_secret=aws_secret)
    print "Beginning new job: %s" % job.jobID
    print "Crawling: %s" % job.crawlPath
    print "Crawl Type: %s" % job.crawlTypeSelected

    result = newJob.apply_async([job],queues="celery")
    logger.info(("Celery ID: %s,Job ID: %s") % (result.id,job.jobID))
    job_result = result.get(timeout=10)
    #logger.info( ("Result: %s") % (job))

def help():
    print 'fasttransfer.py -k <aws key> -s <aws secret key> -n --crawlPath path --crawlKey key'
    print '--key keyaws'
    print '--secret secretaws'
    print '--crawlPath path'
    print '--crawlKey stash:dir:file'
    print '-n (dry run)'
    

def main(argv):
    global aws_secret
    global aws_key
    global DRYRUN
    crawlPath=""
    crawlKey=""
    try:
        opts, args = getopt.getopt(argv,"hnk:s:p:c:",["key=","secret=","crawlPath=","crawlKey="])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-k", "--key"):
            aws_key = arg
        elif opt in ("-s", "--secret"):
            aws_secret = arg
        elif opt in ("-p", "--crawlPath"):
            crawlPath = arg
        elif opt in ("-c", "--crawlKey"):
            crawlKey = arg
        elif opt in ("-n","--dryrun"):
            DRYRUN=True

    if aws_key==None or aws_secret==None or aws_key=="" or aws_secret=="":
        print 'need keys'
        sys.exit()
    else:
        print crawlPath
        startCrawl(crawlPath=crawlPath,crawlKey=crawlKey)
            

if __name__ == "__main__":
    main(sys.argv[1:])