import logging


class Log:
    loglevel = "INFO"
    loglocation = "FastTransfer.log"
    logformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logapp = "FastTransfer"
    logger = None

    def __init__(self,loglevel=None,loglocation=None,logformat=None,logapp=None):
        self.loglevel = loglevel
        self.loglocation = loglocation
        self.logformat = logformat
        self.logapp = logapp

        # create logger
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
