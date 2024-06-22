import logging

# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client

DEBUG = 0
INFO = 1

class Logger():
    logger = None
    request_logger = None

    def __init__(self, level):
        self.logger_level = self._get_logging_level(level)
        # logging.basicConfig(level=self.logger_level)
        if Logger.request_logger is None:
            Logger.request_logger = logging.getLogger("requests.packages.urllib3")
            Logger.request_logger.setLevel(self.logger_level)
            Logger.request_logger.propagate = level

    def getLogger(self):
        # create logger
        if Logger.logger is None:
            Logger.logger = logging.getLogger('Python API')
            Logger.logger.setLevel(self.logger_level)

            ch = logging.StreamHandler()
            ch.setLevel(self.logger_level)

            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)

            # add ch to logger
            Logger.logger.addHandler(ch)

            # http_client.HTTPConnection.debuglevel = 1

        return Logger.logger

    def _get_logging_level(self, level):
        if level is True:
            return logging.DEBUG
        return logging.INFO
