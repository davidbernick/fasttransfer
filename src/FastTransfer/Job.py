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
    logobj = "FastTransfer.Log"
    logger = None
    
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
        self.getConf()
        
        if self.logobj:
            loggingclass = self.get_class(self.logobj)
            if self.logobj == "FastTransfer.Log.Log":
                config = ConfigParser.RawConfigParser()
                try:
                    config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
                    loglevel = config.get('Logging', "loglevel")
                    loglocation = config.get('Logging', "loglocation")
                    logformat = config.get('Logging', "logformat")
                    logapp = config.get('Logging', "logapp")                     
                except Exception,e:
                    raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))
                self.logger = loggingclass(loglevel=loglevel,
                                     loglocation=loglocation,
                                     logformat=logformat,
                                     logapp=logapp)
                self.logger.logger.info("Log Started")
                
        
    def toJson(self):
        return jsonpickle.encode(self,unpicklable=False)

    def get_class(self,kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m    

    def __getstate__(self):
        result = self.__dict__.copy()
        del result['logger']
        return result

    def stashCrawl(self):
        pass
        
    def filesCrawl(self):
        pass

    def dirCrawl(self):
        pass
    
    def getConf(self):
        config = ConfigParser.ConfigParser()
        try:
            config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
            self.bundle_num_files = config.getint('FastTransfer', "bundle_num_files")
            self.bundle_mb = config.getint('FastTransfer', "bundle_mb")
            self.logobj = config.get('FastTransfer', "logobj")
        except Exception,e:
            raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))
