import * as express from 'express'
import * as socketio from 'socket.io'
import {PicastLogger} from './logging'
import {OMXPlayer} from './player'

let logger = new PicastLogger()
let player = new OMXPlayer(logger)

let app = express()
let port = 8000
let server = app.listen(port, () => {
    logger.writeLog('SERVER001', {port: port})
})

let io = socketio(server)

io.on('connect', (socket: socketio.Socket) => {
    console.log(socket.id)

    socket.on('PLAY_VIDEO', (url: string): void => {
        player.initPlayer(url)
    })

    socket.on('STOP_VIDEO', (): void => {
        player.stop()
    })

    socket.on('PLAY_PAUSE', (): void => {
        player.playPause()
    })

    socket.on('PLAYER_STATUS', (callback) => {
        player.status(callback)
    })
})
