express = require 'express'
socketio = require 'socket.io'

Logger = require './src/logger/logging.coffee'
OMXPlayer = require './src/player.coffee'


logger = new Logger()
player = new OMXPlayer(logger)
app = express()

port = 8000
server = app.listen port, () ->
  logger.writeLog('SERVER001', { port: port })

io = socketio(server)


io.on 'connect', (socket) =>
  console.log(socket.id)

  socket.on 'PLAY_VIDEO', (url) =>
    player.play(url)

  socket.on 'STOP_VIDEO', () =>
    player.stop()