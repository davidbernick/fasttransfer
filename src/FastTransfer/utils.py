import ConfigParser,os

def getConf():
        options={}
        config = ConfigParser.ConfigParser()
        try:
            config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
            options["bundle_num_files"] = config.getint('FastTransfer', "bundle_num_files")
            options["bundle_mb"] = config.getint('FastTransfer', "bundle_mb")
            options["logobj"] = config.get('FastTransfer', "logobj")
        except Exception,e:
            raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))
        return options
    
def get_class( kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
            m = getattr(m, comp)            
        return m    

