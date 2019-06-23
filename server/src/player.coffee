execSync = require 'child_process'.execSync
EventEmitter = require 'events'.EventEmitter

{ options, state } = require './player/constants.coffee'


class OMXPlayer extends EventEmitter
  constructor: (logger) ->
    super()
    @logger = logger
    @player = null
    @state = state.idle

  initPlayer: (file) ->
    @player = execSync("omxplayer #{options} #{file}")
    @state = state.playing


  play: (file) ->
    logger.writeLog('PLAYER001', { file: file })
    if @state == state.idle
      @initPlayer(file)
