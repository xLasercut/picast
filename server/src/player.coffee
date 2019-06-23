childProcess = require 'child_process'
EventEmitter = require 'events'.EventEmitter

opts = [ '-o hdmi' ]


class OMXPlayer extends EventEmitter
  constructor: () ->
    super()

