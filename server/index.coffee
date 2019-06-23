express = require 'express'
socketio = require 'socket.io'

Logger = require './src/logger/logging.coffee'


logger = new Logger()
app = express()

port = 8000
server = app.listen port, () ->
  logger.writeLog('SERVER001', { port: port })

io = socketio(server)


io.on 'connect', (socket) =>
  console.log(socket.id)