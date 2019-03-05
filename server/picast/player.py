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
        return self.logger.writeAndReturnLog('CTRL0004')

    def setVolume(self, volume):
        self._checkPlayerExist()
        self.player.set_volume(volume)
        return self.logger.writeAndReturnLog('VOL0003', {'volume': volume})

    def playPause(self):
        self._checkPlayerExist()
        self.player.play_pause()

    def seek(self, seekTime):
        self._checkPlayerExist()
        self.player.seek(seekTime)

    def setPosition(self, position):
        self._checkPlayerExist()
        if position > self.videoLength() or position < 0:
            self._raisePlayerError('SEEK0004', {'position': position})
        self.player.set_position(position)

    def _checkPlayerExist(self):
        if not self.player:
            self._raisePlayerError('CTRL0003')
            
    def videoPosition(self):
        self._checkPlayerExist()
        return self.player.position()
    
    def videoLength(self):
        self._checkPlayerExist()
        return self.player.duration() 
    
    def videoVolume(self):
        self._checkPlayerExist()
        return self.player.volume()
    
    def playbackStatus(self):
        self._checkPlayerExist()
        return self.player.playback_status()

    def _raisePlayerError(self, logReference, variablesDict={}):
        returnMsg = self.logger.writeAndReturnLog(logReference, variablesDict)
        raise PlayerError(returnMsg)
