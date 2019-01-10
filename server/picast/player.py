from omxplayer.player import OMXPlayer

class VideoPlayer(object):

    def __init__(self):
        self.player = None

    def playUrl(self, url):
        if not self.player:
            self.player = OMXPlayer(url)
        else:
            self.player.load(url)

    def stop(self):
        self.player.quit()

    def setVolume(self, volume):
        self.player.set_volume(volume)

    def playPause(self):
        self.player.play_pause()

    def seek(self, seekTime):
        self.player.seek(seekTime)
