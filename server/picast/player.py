from omxplayer.player import OMXPlayer
from picast.exceptions import PlayerError
from picast.logging import LogObject

class VideoPlayer(object):

    def __init__(self):
        self.player = None
        self.logger = LogObject('Video Player')

    def playUrl(self, url):
        if not self.player:
            self.player = OMXPlayer(url)
        else:
            self.player.load(url)

    def stop(self):
        self._checkPlayerExist()
        self.player.quit()

    def setVolume(self, volume):
        self._checkPlayerExist()
        self.player.set_volume(volume)

    def playPause(self):
        self._checkPlayerExist()
        self.player.play_pause()

    def seek(self, seekTime):
        self._checkPlayerExist()
        self.player.seek(seekTime)

    def setPosition(self, position):
        self._checkPlayerExist()
        if position > self._videoLength or position < 0:
            self._raisePlayerError('PLAYER0001', {'position': position})
        self.player.set_position(position)

    def _checkPlayerExist(self):
        if not self.player:
            self._raisePlayerError('PLAYER0002')

    @property
    def _videoLength(self):
        metadata = self.player.metadata()
        return metadata.get('mpris:length')/1000000

    def _raisePlayerError(self, logReference, variablesDict={}):
        returnMsg = self.logger.writeAndReturnLog(logReference, variablesDict)
        raise PlayerError(returnMsg)
