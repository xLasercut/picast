import logging
import configparser
import pystache

from picast import app

class LogObject(object):

    LOG_FORMAT = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    VALID_LOG_LEVEL = ['INFO', 'WARN', 'ERROR', 'CRIT']

    def __init__(self, applicationName, logPath=app.config['LOG_PATH'], logBase=app.config['LOG_BASE']):
        self.logFormatter = logging.Formatter(self.LOG_FORMAT)
        self.logPath = logPath
        self.logger = logging.getLogger(applicationName)
        self._initialiseLogging()
        self.logBase = self._initialiseLogBase(logBase)

    def writeLog(self, logReference, variablesDict={}):
        logLevel, logMessage = self._getLogDetails(logReference, variablesDict)
        self._renderLog(logLevel, logMessage)

    def writeAndReturnLog(self, logReference, variablesDict={}):
        logLevel, logMessage = self._getLogDetails(logReference, variablesDict)
        self._renderLog(logLevel, logMessage)
        return logMessage

    def debug(self, debugMsg):
        self.logger.debug(debugMsg)

    @staticmethod
    def _initialiseLogBase(logBase):
        config = configparser.ConfigParser()
        config.read(logBase)
        return config

    def _initialiseLogging(self):
        fileHandler = logging.FileHandler(self.logPath)
        fileHandler.setFormatter(self.logFormatter)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(self.logFormatter)

        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(consoleHandler)

    def _getLogDetails(self, logReference, variablesDict={}):
        try:
            logDict = self.logBase[logReference]
            logLevel = logDict['Log Level']
            logText = logDict['Log Text']
            if not logLevel or not logText or logLevel not in self.VALID_LOG_LEVEL:
                raise KeyError
            logMessage = pystache.render(logText, variablesDict)
            return logLevel, logMessage
        except KeyError:
            return 'ERROR', 'Log Reference: {} is invalid'.format(logReference)

    def _renderLog(self, logLevel, logMessage):
        if logLevel == 'INFO':
            self.logger.info(logMessage)
        elif logLevel == 'WARN':
            self.logger.warning(logMessage)
        elif logLevel == 'ERROR':
            self.logger.error(logMessage)
        elif logLevel == 'CRIT':
            self.logger.critical(logMessage)
