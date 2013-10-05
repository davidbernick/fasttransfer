import os

class Dir:
    path = None
    parent = None
    def __init__(self,filepath=None):
        self.path = filepath
        self.parent = os.path.split(os.path.abspath(filepath))[0]
    
    def browse_by_path(self,path="/"):
        #
        pass
    
    def browse_by_tag(self,path="/"):
        #
        pass    