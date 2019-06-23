{ exec } = require 'child_process'

{ options, state, controls } = require './player/constants.coffee'


class OMXPlayer
  constructor: (logger) ->
    @logger = logger
    @player = null
    @state = state.idle

  initPlayer: (file) ->
    @player = exec("omxplayer #{options} #{file}")
    @state = state.playing


  play: (file) ->
    @logger.writeLog('PLAYER001', { file: file })
    if @state == state.idle
      @initPlayer(file)

  stop: () ->
    @sendKey(controls.stop)

  sendKey: (key) ->
    console.log(@player)
    if !@player or @state == state.idle
      return false

    @player.stdin.write(key)


module.exports = OMXPlayer