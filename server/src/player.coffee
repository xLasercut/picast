{ exec } = require 'child_process'
path = require 'path'
q = require 'q'

{ options, state, controls, dbus } = require './player/constants.coffee'

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
    @_sendKey(controls.stop)
    @resetPlayer()


  playPause: () ->
    @_sendKey(controls.pause)
    if @state == state.playing
      @state = state.paused
    else if @state == state.paused
      @state = state.playing

  seek: (position, callback) ->
    @_sendDbusControl(dbus.seek, position, callback)

  resetPlayer: () ->
    @player = null
    @file = null
    @state = state.idle

  status: (callback) ->
    @_sendDbusControl dbus.status, null, (data) =>
      output = {}
      for row in data.split('\n')
        if row
          rowArray = row.split(':')
          output[rowArray[0]] = rowArray[1].trim()
      callback(output)

  volume: (callback) ->
    @_sendDbusControl dbus.volume, null, (data) =>
      callback(data)

  _sendKey: (key) ->
    @logger.writeLog('PLAYER002', { key: key })
    if !@player or @state == state.idle
      return false

    @player.stdin.write(key)

  _sendDbusControl: (command, value, callback) ->
    if value
      cmd = "#{controlFile} #{command} #{value}"
    else
      cmd = "#{controlFile} #{command}"

    exec cmd, (err, stdout, stderr) =>
      if stderr
        @logger.writeLog('PLAYER003', { error: stderr })
      else
        callback(stdout)

module.exports = OMXPlayer