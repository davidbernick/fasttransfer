import logging,os,ConfigParser
from .utils import getConf,get_class

class Log:
    loglevel = "INFO"
    loglocation = "FastTransfer.log"
    logformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logapp = "FastTransfer"
    logger = None

    @classmethod
    def getLog(self):
        logobj = getConf()["logobj"]
        config = ConfigParser.RawConfigParser()
        if logobj:
            #loggingclass = get_class(logobj)
            if logobj == "FastTransfer.Log.Log":
                try:
                    config.read(os.path.expanduser("~")+'/.fasttransfer.conf')
                    self.loglevel = config.get('Logging', "loglevel")
                    self.loglocation = config.get('Logging', "loglocation")
                    self.logformat = config.get('Logging', "logformat")
                    self.logapp = config.get('Logging', "logapp")                     
                except Exception,e:
                    raise Exception("Need valid ~/.fasttransfer.conf: %s" % (e))
                
                self.logger = logging.getLogger(self.logapp)
                self.logger.setLevel(self.loglevel)
                
                # add a file handler
                fh = logging.FileHandler(self.loglocation)
                fh.setLevel(self.loglevel)
                # create a formatter and set the formatter for the handler.
                frmt = logging.Formatter(self.logformat)
                fh.setFormatter(frmt)
                # add the Handler to the logger
                self.logger.addHandler(fh)
                
                return self.logger
