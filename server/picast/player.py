from omxplayer.player import OMXPlayer
from picast.exceptions import InvalidRequest, ErrorConstants

class VideoPlayer(object):

    def __init__(self):
        self.player = None

    def playUrl(self, url):
        if not self.player:
            self.player = OMXPlayer(url)
        else:
            self.player.load(url)

    def stop(self):
        self._checkVideoExists()
        self.player.quit()

    def setVolume(self, volume):
        self._checkVideoExists()
        self.player.set_volume(volume)

    def playPause(self):
        self._checkVideoExists()
        self.player.play_pause()

    def seek(self, seekTime):
        self._checkVideoExists()
        self.player.seek(seekTime)

    def _checkVideoExists(self):
        if not self.player:
            raise InvalidRequest(ErrorConstants.EMPTY_VIDEO)
