{ execSync } = require 'child_process'

{ options, state } = require './player/constants.coffee'


class OMXPlayer
  constructor: (logger) ->
    @logger = logger
    @player = null
    @state = state.idle

  initPlayer: (file) ->
    @player = execSync("omxplayer #{options} #{file}")
    @state = state.playing


  play: (file) ->
    @logger.writeLog('PLAYER001', { file: file })
    if @state == state.idle
      @initPlayer(file)


module.exports = OMXPlayer