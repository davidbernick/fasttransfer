from collections import deque
import uuid
import ConfigParser,os.path,httplib, urllib, urllib2, cookielib,base64,json
import jsonpickle

crawlType={
           "stash":0,
           "dir":1,
           "file":2
           }


class Job:
    
    FileContainerCollection = None
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
        self.FileContainerCollection = deque()
        self.crawlPath = crawlPath
        self.jobID = str(uuid.uuid4())
        self.crawlTypeSelected = crawlType[crawlKey]
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        
        config = ConfigParser.ConfigParser()
        try:
            config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
            self.bundle_num_files = config.getint('FastTransfer', "bundle_num_files")
            self.bundle_mb = config.getint('FastTransfer', "bundle_mb")
        except Exception,e:
            raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))
        
    def toJson(self):
        return jsonpickle.encode(self)
        
