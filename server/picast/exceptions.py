class ErrorConstants(object):
    EMPTY_REQUEST = "No request body found"
    INVALID_URL = "'{0}' is not a valid URL"
    EMPTY_URL = "No URL supplied"
    INVALID_VOLUME = "Volume must be a number between 0 and 10"
    EMPTY_VOLUME = "No volume value supplied"
    INVALID_SEEK = "Seek Time must be a number"
    EMPTY_SEEK = "No Seek Time supplied"
    EMPTY_VIDEO = "Cannot issue control commands when no video is playing"

class AbstractException(Exception):
    def __init__(self, message):
        self.message = message
        self.httpCode = 500

    def sendErrorResponse(self):
        return self.message, self.httpCode

class InvalidRequest(AbstractException):
    def __init__(self, message):
        super(InvalidRequest, self).__init__(message)
        self.httpCode = 403
