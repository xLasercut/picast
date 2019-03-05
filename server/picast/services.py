import re
import youtube_dl

from picast.exceptions import InvalidRequest, PlayerError
from picast.player import VideoPlayer
from picast.logging import LogObject
from flask import jsonify

player = VideoPlayer()

class AbstractService(object):
    def __init__(self, request):
        self.request = request.get_json()
        self._checkEmptyRequestBody()

    def runWorkflow(self):
        self._validateRequest()
        try:
            self._processRequest()
        except PlayerError as e:
            raise InvalidRequest(e.errorResponse)

    @property
    def successResponse(self):
        return self.successMsg, 200
    
    def _checkEmptyRequestBody(self):
        if not self.request:
            self._raiseServiceError('REQ0001')

    def _validateRequest(self):
        pass

    def _processRequest(self):
        pass

    def _raiseServiceError(self, logReference, variablesDict={}):
        returnMsg = self.logger.writeAndReturnLog(logReference, variablesDict)
        raise InvalidRequest(returnMsg)
    
class StatusService(AbstractService):
    STATUS_MAP = {
        'length': player.videoLength,
        'volume': player.videoVolume,
        'playback': player.playbackStatus,
        'position': player.videoPosition
    }
    
    
    def __init__(self, request):
        self.logger = LogObject('Status Service')
        super(StatusService, self).__init__(request)
        self.requiredStatus = self.request.get('status', [])
        
    def _validateRequest(self):
        if not isinstance(self.requiredStatus, list):
            self._raiseServiceError('STAT0002')
        
        for status in self.requiredStatus:
            if status not in self.STATUS_MAP:
                self._raiseServiceError('STAT0001', {'status': status})
                
    def _processRequest(self):
        if not self.requiredStatus:
            self.successMsg = 'OK'
        else:
            try:
                returnDict = {}
                for status in self.requiredStatus:
                    returnDict[status] = self.STATUS_MAP[status]()
                self.successMsg = jsonify(returnDict)
            except PlayerError as e:
                raise InvalidRequest(e.errorResponse)
        
    def _checkEmptyRequestBody(self):
        if not self.request:
            self.request = {}

class StreamService(AbstractService):
    VIDEO_QUALITY = {
        '240p': {'height': 240, 'width': 320},
        '360p': {'height': 360, 'width': 480 },
        '480p': {'height': 480, 'width': 720},
        '720p': {'height': 720, 'width': 1280},
        '1080p': {'height': 1080, 'width': 1920}
    }

    VIDEO_ENDING = re.compile(r'(\.mp4|\.mkv|.mov)$', re.IGNORECASE)
    
    def __init__(self, request):
        self.logger = LogObject('Stream Service')
        super(StreamService, self).__init__(request)
        self.url = self.request.get('url')
        self.quality = self.request.get('quality', '720p')
        self.format = self.request.get('format', 'mp4')
        self.streamUrl = ''

    def _validateRequest(self):
        if not self.url:
            self._raiseServiceError('URL0002')

        if self.quality not in self.VIDEO_QUALITY:
            self._raiseServiceError('QUALITY0001', {'quality': self.quality})

        self._parseUrl()
                
        if not self.streamUrl:
            self._raiseServiceError('URL0003')

    def _processRequest(self):
        player.playUrl(self.streamUrl)
        self.successMsg = self.logger.writeAndReturnLog('URL0004', {'url': self.url})
        
    def _parseUrl(self):
        if self.VIDEO_ENDING.search(self.url):
            self.streamUrl = self.url
            
        self.streamUrl = self._extractVideoUrl()

    def _extractVideoUrl(self):
        with youtube_dl.YoutubeDL({}) as ydl:
            infoDict = ydl.extract_info(self.url, download=False)
            for video in infoDict.get('formats'):
                if self._isCorrectFormat(video):
                    return video.get('url')
            return None

    def _isCorrectFormat(self, video):
        videoQuality = {
            'height': video.get('height'),
            'width': video.get('width')
        }
        requiredQualiy = self.VIDEO_QUALITY.get(self.quality)
        ext = video.get('ext')
        if videoQuality == requiredQualiy and ext == self.format:
            return True
        return False

class VolumeService(AbstractService):

    def __init__(self, request):
        self.logger = LogObject('Volume Service')
        super(VolumeService, self).__init__(request)
        self.volume = self.request.get('volume')

    def _validateRequest(self):
        if self.volume is None:
            self._raiseServiceError('VOL0002')

        try:
            self.volume = float(self.volume)
        except ValueError:
            self._raiseServiceError('VOL0001')

        if self.volume < 0 or self.volume > 10:
            self._raiseServiceError('VOL0001')

    def _processRequest(self):
        self.successMsg = player.setVolume(self.volume)

class SeekService(AbstractService):
    CONTROL_MAP = {
        'relative': player.seek,
        'absolute': player.setPosition
    }

    def __init__(self, request):
        self.logger = LogObject('Seek Service')
        super(SeekService, self).__init__(request)
        self.time = self.request.get('time')
        self.option = self.request.get('option')

    def _validateRequest(self):
        if not self.time or not self.option:
            self._raiseServiceError('SEEK0002')

        if self.option not in self.CONTROL_MAP:
            self._raiseServiceError('SEEK0003', {'option': self.option})

        try:
            self.time = int(self.time)
        except ValueError:
            self._raiseServiceError('SEEK0001')

    def _processRequest(self):
        player.seek(self.time)
        self.successMsg = 'seek'


class ControlService(AbstractService):
    CONTROL_MAP = {
        'stop': player.stop,
        'playpause': player.playPause
    }

    def __init__(self, request):
        self.logger = LogObject('Control Service')
        super(ControlService, self).__init__(request)
        self.option = self.request.get('option')

    def _validateRequest(self):
        if not self.option:
            self._raiseServiceError('CTRL0001')

        if self.option not in self.CONTROL_MAP:
            self._raiseServiceError('CTRL0002', {'option': self.option})

    def _processRequest(self):
        self.successMsg = self.CONTROL_MAP[self.option]()
