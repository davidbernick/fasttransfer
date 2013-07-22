
class FileContainer(list):
    
    numfiles = 0
    containersize = 0
    
    def __init__(self):
        self.numfiles = 0
        self.containersize = 0
            
    def addFileSize(self,newsize):
        self.containersize=self.containersize+newsize
        return self.containersize
    
    def addNumFile(self):
        self.numfiles=self.numfiles+1
        return self.numfiles
    
    def addFile(self,f):
        self.append(f)
        self.addFileSize(f["size"])
        self.addNumFile()
