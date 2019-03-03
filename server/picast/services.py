import youtube_dl

from picast.exceptions import InvalidRequest, PlayerError
from picast import app
from picast.player import VideoPlayer
from picast.logging import LogObject

from flask import jsonify

player = VideoPlayer()

class AbstractService(object):
    def __init__(self, request):
        self.request = request.get_json()
        if not self.request:
            self._raiseServiceError('REQ0001')

    def runWorkflow(self):
        self._validateRequest()
        try:
            self._processRequest()
        except PlayerError as e:
            raise InvalidRequest(e.errorResponse)

    @property
    def successResponse(self):
        return self.successMsg, 200

    def _validateRequest(self):
        pass

    def _processRequest(self):
        pass

    def _raiseServiceError(self, logReference, variablesDict={}):
        returnMsg = self.logger.writeAndReturnLog(logReference, variablesDict)
        raise InvalidRequest(returnMsg)

class StreamService(AbstractService):
    VIDEO_QUALITY = {
        '240p': {'height': 240, 'width': 320},
        '360p': {'height': 360, 'width': 480 },
        '480p': {'height': 480, 'width': 720},
        '720p': {'height': 720, 'width': 1280},
        '1080p': {'height': 1080, 'width': 1920}
    }

    VIDEO_EXTENTIONS = ['mp4']

    def __init__(self, request):
        self.logger = LogObject('Stream Service')
        super(StreamService, self).__init__(request)
        self.streamUrl = self.request.get('streamUrl')
        self.streamQuality = self.request.get('streamQuality', '720p')

    def _validateRequest(self):
        if not self.streamUrl:
            self._raiseServiceError('URL0002')

        if self.streamQuality not in self.VIDEO_QUALITY:
            self._raiseServiceError('QUALITY0001', {'quality': self.streamQuality})

        self.streamUrl = self._extractVideoUrl()
        if not self.streamUrl:
            self._raiseServiceError('URL0003')

        self.successMsg = self.streamUrl

    def _processRequest(self):
        player.playUrl(self.streamUrl)
        self.successMsg = self.logger.writeAndReturnLog('URL0004', {'url': self.streamUrl})

    def _extractVideoUrl(self):
        with youtube_dl.YoutubeDL({}) as ydl:
            infoDict = ydl.extract_info(self.streamUrl, download=False)
            for video in infoDict.get('formats'):
                if self._isCorrectFormat(video):
                    return video.get('url')
            return None

    def _isCorrectFormat(self, video):
        videoQuality = {
            'height': video.get('height'),
            'width': video.get('width')
        }
        requiredQualiy = self.VIDEO_QUALITY.get(self.streamQuality)
        ext = video.get('ext')
        if videoQuality == requiredQualiy and ext in self.VIDEO_EXTENTIONS:
            return True
        return False

class VolumeService(AbstractService):

    def __init__(self, request):
        self.logger = LogObject('Volume Service')
        super(VolumeService, self).__init__(request)
        self.volumeLevel = self.request.get('volumeLevel')

    def _validateRequest(self):
        if self.volumeLevel is None:
            self._raiseServiceError('VOL0002')

        try:
            self.volumeLevel = float(self.volumeLevel)
        except ValueError:
            self._raiseServiceError('VOL0001')

        if self.volumeLevel < 0 or self.volumeLevel > 10:
            self._raiseServiceError('VOL0001')

    def _processRequest(self):
        player.setVolume(self.volumeLevel)
        self.successMsg = 'volume set to {0}'.format(self.volumeLevel)

class SeekService(AbstractService):
    CONTROL_MAP = {
        'relative': player.seek,
        'absolute': player.setPosition
    }

    def __init__(self, request):
        self.logger = LogObject('Seek Service')
        super(SeekService, self).__init__(request)
        self.seekTime = self.request.get('seekTime')
        self.seekOption = self.request.get('seekOption')

    def _validateRequest(self):
        if not self.seekTime or not self.seekOption:
            self._raiseServiceError('SEEK0002')

        if self.seekOption not in self.CONTROL_MAP:
            self._raiseServiceError('SEEK0003', {'option': self.seekOption})

        try:
            self.seekTime = int(self.seekTime)
        except ValueError:
            self._raiseServiceError('SEEK0001')

    def _processRequest(self):
        player.seek(self.seekTime)
        self.successMsg = 'seek'


class ControlService(AbstractService):
    CONTROL_MAP = {
        'stop': player.stop,
        'pause': player.playPause
    }

    def __init__(self, request):
        self.logger = LogObject('Control Service')
        super(ControlService, self).__init__(request)
        self.controlOption = self.request.get('controlOption')

    def _validateRequest(self):
        if not self.controlOption:
            self._raiseServiceError('CTRL0001')

        if self.controlOption not in self.CONTROL_MAP:
            self._raiseServiceError('CTRL0002', {'option': self.controlOption})

    def _processRequest(self):
        self.CONTROL_MAP[self.controlOption]()
        self.successMsg = 'control'
