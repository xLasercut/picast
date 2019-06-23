{ exec } = require 'child_process'
path = require 'path'
q = require 'q'

{ options, state, controls } = require './player/constants.coffee'

controlFile = path.join(__dirname, 'player', 'dbuscontrol.sh')

class OMXPlayer
  constructor: (logger) ->
    @logger = logger
    @player = null
    @state = state.idle
    @file = null

  initPlayer: (file) ->
    @logger.writeLog('PLAYER001', { file: file })
    @player = exec("omxplayer #{options} #{file}")
    @state = state.playing
    @file = file

  stop: () ->
    @sendKey(controls.stop)
    @resetPlayer()


  playPause: () ->
    @sendKey(controls.pause)
    if @state == state.playing
      @state = state.paused
    else if @state == state.paused
      @state = state.playing

  sendKey: (key) ->
    @logger.writeLog('PLAYER002', { key: key })
    if !@player or @state == state.idle
      return false

    @player.stdin.write(key)

  seek: (position) ->
    if !@file
      return false

    file = @file
    if @player or @state != state.idle
      @stop()

    @player = exec("omxplayer #{options} #{file}")

  resetPlayer: () ->
    @player = null
    @file = null
    @state = state.idle

  status: (callback) ->
    exec("#{controlFile} status", callback)

module.exports = OMXPlayer