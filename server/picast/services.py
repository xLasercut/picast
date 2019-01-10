import re

from picast.exceptions import ErrorConstants, InvalidRequest
from picast import app
from picast.player import VideoPlayer

player = VideoPlayer()

class AbstractService(object):
    def __init__(self, request):
        self.request = request.get_json()
        if not self.request:
            raise InvalidRequest(ErrorConstants.EMPTY_REQUEST)

    def runWorkflow(self):
        self.validateRequest()
        self.processRequest()

    def validateRequest(self):
        pass

    def processRequest(self):
        pass

    @property
    def successResponse(self):
        return self.successMsg, 200

class StreamService(AbstractService):

    URL_PATTERN = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __init__(self, request):
        super(StreamService, self).__init__(request)
        self.streamUrl = self.request.get("streamUrl")

    def validateRequest(self):
        if not self.streamUrl:
            raise InvalidRequest(ErrorConstants.EMPTY_URL)

        #if not self.URL_PATTERN.match(self.streamUrl):
        #    raise InvalidRequest(ErrorConstants.INVALID_URL.format(self.streamUrl))

    def processRequest(self):
        player.playUrl(self.streamUrl)
        self.successMsg = "url {0} stream success".format(self.streamUrl)

class VolumeService(AbstractService):

    def __init__(self, request):
        super(VolumeService, self).__init__(request)
        self.volumeLevel = self.request.get("volumeLevel")

    def validateRequest(self):
        if self.volumeLevel is None:
            raise InvalidRequest(ErrorConstants.EMPTY_VOLUME)

        try:
            self.volumeLevel = float(self.volumeLevel)
        except ValueError:
            raise InvalidRequest(ErrorConstants.INVALID_VOLUME)

        if self.volumeLevel < 0 or self.volumeLevel > 10:
            raise InvalidRequest(ErrorConstants.INVALID_VOLUME)

    def processRequest(self):
        player.setVolume(self.volumeLevel)
        self.successMsg = "volume set to {0}".format(self.volumeLevel)

class SeekService(AbstractService):
    def __init__(self, request):
        super(SeekService, self).__init__(request)
        self.seekTime = self.request.get("seekTime")

    def validateRequest(self):
        if not self.seekTime:
            raise InvalidRequest(ErrorConstants.EMPTY_SEEK)

        try:
            self.seekTime = int(self.seekTime)
        except ValueError:
            raise InvalidRequest(ErrorConstants.INVALID_SEEK)

    def processRequest(self):
        player.seek(self.seekTime)
        self.successMsg = "seek"


class ControlService(AbstractService):
    def __init__(self, request):
        super(ControlService, self).__init__(request)
        self.controlOption = self.request.get("controlOption")

    def validateRequest(self):
        if not self.controlOption:
            raise InvalidRequest("No options given")

    def processRequest(self):
        if self.controlOption == "stop":
            player.stop()
        elif self.controlOption == "pause":
            player.playPause()
        self.successMsg = "control"
