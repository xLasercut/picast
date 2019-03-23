from omxplayer.player import OMXPlayer, OMXPlayerDeadError
from picast.exceptions import PlayerError
from picast.logging import LogObject

class VideoPlayer(object):

    def __init__(self):
        self.player = None
        self.logger = LogObject('Video Player')
        self.args = ['-b']
        
        self.STATUS_MAP = {
            'volume': self._videoVolume,
            'length': self._videoLength,
            'playback': self._playbackStatus,
            'position': self._videoPosition
        }
        
        self.CONTROL_MAP = {
            'playpause': self._playPause,
            'stop': self._stop,
            'mute': self._mute,
            'unmute': self._unmute,
            'play': self._play,
            'pause': self._pause
        }

        self.SEEK_MAP = {
            'relative': self._seek,
            'absolute': self._setPosition
        }

    def playUrl(self, url):

        if not self.player:
            self.player = OMXPlayer(url, args=self.args)
        else:
            try:
                self.player.load(url)
            except OMXPlayerDeadError:
                self.player = OMXPlayer(url, args=self.args)
            
    def setVolume(self, volume):
        self._checkPlayerExist()
        try:
            self.player.set_volume(volume)
            return self.logger.writeAndReturnLog('VOL0003', {'volume': volume})
        except AttributeError, OMXPlayerDeadError:
            self._raisePlayerError('VOL0004')
    
    def sendCommand(self, command):
        self._checkPlayerExist()
        try:
            return self.CONTROL_MAP[command]()
        except AttributeError, OMXPlayerDeadError:
            self._raisePlayerError('CTRL0003')

    def _stop(self):
        self.player.quit()
        return self.logger.writeAndReturnLog('CTRL0004')
    
    def _mute(self):
        self.player.mute()
        return self.logger.writeAndReturnLog('CTRL0006')

    def _unmute(self):
        self.player.unmute()
        return self.logger.writeAndReturnLog('CTRL0007')

    def _playPause(self):
        self.player.play_pause()
        return self.logger.writeAndReturnLog('CTRL0005')

    def _play(self):
        self.player.play()
        return self.logger.writeAndReturnLog('CTRL0008')

    def _pause(self):
        self.player.pause()
        return self.logger.writeAndReturnLog('CTRL0009')
    
    def seek(self, option, time):
        self._checkPlayerExist()
        try:
            return self.SEEK_MAP[option](time)
        except AttributeError, OMXPlayerDeadError:
            self._raisePlayerError('SEEK0007')

    def _seek(self, seekTime):
        self.player.seek(seekTime)
        return self.logger.writeAndReturnLog('SEEK0005', {'position': seekTime})

    def _setPosition(self, position):
        if position > self._videoLength() or position < 0:
            self._raisePlayerError('SEEK0004', {'position': position})
        self.player.set_position(position)
        return self.logger.writeAndReturnLog('SEEK0006', {'position': position})

    def _checkPlayerExist(self):
        if not self.player:
            self._raisePlayerError('CTRL0003')
            
    def videoStatus(self, status):
        if not self.player:
            self._raisePlayerError('STAT0003')
        try:
            return self.STATUS_MAP[status]()
        except AttributeError, OMXPlayerDeadError:
            self._raisePlayerError('STAT0003')
        
    def _videoPosition(self):
        return self.player.position()
    
    def _videoLength(self):
        return self.player.duration() 
    
    def _videoVolume(self):
        return self.player.volume()
    
    def _playbackStatus(self):
        return self.player.playback_status()

    def _raisePlayerError(self, logReference, variablesDict={}):
        returnMsg = self.logger.writeAndReturnLog(logReference, variablesDict)
        raise PlayerError(returnMsg)
