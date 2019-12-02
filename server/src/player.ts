import * as q from 'q'
import {exec} from 'child_process'
import {CONTROLS, DBUS, OPTIONS, STATE} from './shared/configs/player'
import {PLAYER_CONTROL_FILE} from './shared/configs/paths'
import {PicastLogger} from './logging'

class OMXPlayer {
    private _logger: PicastLogger
    private _player
    private _state: number = STATE.idle
    private _file: string

    constructor(logger: PicastLogger) {
        this._logger = logger
    }

    initPlayer(file: string): void {
        this._logger.writeLog('PLAYER001', {file: file})
        this._player = exec(`omxplayer ${OPTIONS} ${file}`)
        this._state = STATE.playing
        this._file = file
    }

    resetPlayer(): void {
        this._player = null
        this._file = null
        this._state = STATE.idle
    }

    stop(): void {
        this._sendKey(CONTROLS.stop)
        this.resetPlayer()
    }

    playPause(): void {
        this._sendKey(CONTROLS.pause)
        if (this._state === STATE.playing) {
            this._state = STATE.paused
        }
        else if (this._state === STATE.paused) {
            this._state = STATE.playing
        }
    }

    seek(position: string): void {
        this._sendDbusControl(DBUS.seek, position)
    }

    status(callback) {
        let output = {}
        this._sendDbusControl(DBUS.status)
            .then((data) => {
                for (let row in data.split('\n')) {
                    if (row) {
                        let rowArray = row.split(':')
                        output[rowArray[0]] = rowArray[1].trim()
                    }
                }
                return this._sendDbusControl(DBUS.volume)
            })
            .then((data) => {
                let array = data.split(':')
                output[array[0]] = array[1].trim()
                callback(output)
            })
    }

    _sendKey(key: string): boolean {
        this._logger.writeLog('PLAYER002', {key: key})
        if (!this._player || this._state === STATE.idle) {
            return false
        }
        this._player.stdin.write(key)
    }

    _sendDbusControl(command: string, value: string = null) {
        let deferred = q.defer()
        let cmd = `${PLAYER_CONTROL_FILE} ${command}`
        if (value) {
            cmd = `${PLAYER_CONTROL_FILE} ${command} ${value}`
        }

        exec(cmd, (err, stdout, stderr) => {
            if (stderr) {
                this._logger.writeLog('PLAYER003', { error: stderr })
            }
            else {
                deferred.resolve(stdout)
            }
        })

        return deferred.promise
    }
}


export {OMXPlayer}
