from omxplayer.player import OMXPlayer
from picast.exceptions import PlayerError

class VideoPlayer(object):

    def __init__(self):
        self.player = None

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
            raise PlayerError(PlayerError.INVALID_VIDEO_POSITION)
        self.player.set_position(position)

    def _checkPlayerExist(self):
        if not self.player:
            raise PlayerError(PlayerError.EMPTY_VIDEO)

    @property
    def _videoLength(self):
        metadata = self.player.metadata()
        return metadata.get("mpris:length")/1000000
