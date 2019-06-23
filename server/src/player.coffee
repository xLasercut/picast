childProcess = require 'child_process'
EventEmitter = require 'events'.EventEmitter

{ options, state } = require './player/map.coffee'


class OMXPlayer extends EventEmitter
  constructor: () ->
    super()
    @player = childProcess.execSync("omxplayer #{options}")
    @state = state.idle
