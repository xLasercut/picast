class AbstractException(Exception):
    def __init__(self, message, httpCode=None):
        self.message = message
        self.httpCode = httpCode

    @property
    def errorResponse(self):
        if not self.httpCode:
            return self.message
        return self.message, self.httpCode

class InvalidRequest(AbstractException):
    def __init__(self, message):
        super(InvalidRequest, self).__init__(message, 403)

class PlayerError(AbstractException):
    def __init__(self, message):
        super(PlayerError, self).__init__(message)
