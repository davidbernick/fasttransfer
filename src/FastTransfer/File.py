import os
from FastTransfer.Dir import Dir

class File(dict):
    
    def __init__(self,filepath=None,statinfo=None):
        self["filepath"]=filepath
        self["dirpath"]=os.path.dirname(filepath)
        
        self["size"]=statinfo.st_size
        self["uid"]=statinfo.st_uid
        self["gid"]=statinfo.st_gid
        self["mode"]=statinfo.st_mode
        self["mtime"]=statinfo.st_mtime
        self["ctime"]=statinfo.st_ctime
        self["dir"]=os.path.dirname(filepath)
        
    def getTags(self):
        return self
          
