class InvalidRequest(Exception):
    EMPTY_REQUEST = "No request body found"
    INVALID_URL = "'{0}' is not a valid URL"
    EMPTY_URL = "No URL supplied"
    INVALID_VOLUME = "Volume must be a number between 0 and 10"
    EMPTY_VOLUME = "No volume value supplied"
    INVALID_SEEK = "Seek Time must be a number"
    EMPTY_SEEK = "No Seek Time supplied"

    def __init__(self, message):
        self.message = message

    @property
    def errorResponse(self):
        return self.message, 403

class PlayerError(Exception):
    EMPTY_VIDEO = "Cannot issue control commands when no video is playing"
    INVALID_VIDEO_POSITION = "Seek position outside video length"

    def __init__(self, message):
        self.message = message

    @property
    def errorResponse(self):
        return self.message
