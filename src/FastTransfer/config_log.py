import logging.config
import os.path
LOGGING_CONF=os.path.join(os.path.expanduser("~")+"/logconfig.ini")

logging.config.fileConfig(LOGGING_CONF)