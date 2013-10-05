from collections import deque
import uuid
import ConfigParser,os.path,httplib, urllib, urllib2, cookielib,base64,json,os
from FastTransfer.FileContainer import FileContainer
from FastTransfer.File import File
import jsonpickle
from .utils import getConf
import config_log
import logging


crawlType={
           "stash":0,
           "dir":1,
           "file":2
           }

logger = logging.getLogger("job")

class Job:
    global logger
    FileContainerCollection = []
    crawlPath = None
    jobID = None
    crawlTypeSelected=None
    aws_key = None
    aws_secret = None
    bundle_num_files = 1000
    bundle_mb = 1000
    
    def __init__(self,crawlPath=None,
                 crawlKey=None,
                 aws_key=None,
                 aws_secret=None):
        self.FileContainerCollection = []
        self.crawlPath = crawlPath
        self.jobID = str(uuid.uuid4())
        self.crawlTypeSelected = crawlType[crawlKey]
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        conf = getConf()
        try:
            self.bundle_num_files=conf["bundle_num_files"]
        except:
            pass
        try:
            self.bundle_mb=conf["bundle_mb"]
        except:
            pass


    #Used for building crawls that stash everytime it hits a limit.
    def stashCrawl(self):
        from FastTransfer.tasks import processFileContainer
        fc = FileContainer()
        for (path, dirs, files) in os.walk(self.crawlPath):
            for fi in files:
                kilo_byte_size = fc.containersize/1024
                mega_byte_size = kilo_byte_size/1024
                rfile = os.path.join(path,fi)
                if os.path.islink(rfile):
                    continue
                statinfo = os.stat(rfile)
                if fc.numfiles<self.bundle_num_files and mega_byte_size<self.bundle_mb:
                    f = File(filepath=rfile,statinfo=statinfo)
                    fc.addFile(f)
                    logger.debug("Size %s MB %s" % (mega_byte_size,fc.numfiles))
                    continue
                else:
                    logger.debug("New Job")
                    self.FileContainerCollection.append(fc)
                    fc = FileContainer()
                    f = File(filepath=rfile,statinfo=statinfo)
                    fc.addFile(f)
                    continue
        #put final stuff in    
        logger.info("Remaining: %s MB %s Files" % (fc.containersize,fc.numfiles))
        self.FileContainerCollection.append(fc)
        for fc in self.FileContainerCollection:
            processFileContainer.apply_async([fc],queue="files")
        return self
        
    def filesCrawl(self):
        return

    def dirCrawl(self):
        return

        
    def toJson(self):
        return jsonpickle.encode(self,unpicklable=False)

        