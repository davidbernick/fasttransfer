from collections import deque
import uuid

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
        
