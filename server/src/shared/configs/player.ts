let OPTIONS = [ '-o hdmi' ]

let STATE = {
    playing: 0,
    paused: 1,
    idle: 2
}

let CONTROLS = {
    stop: 'q',
    pause: 'p'
}

let DBUS = {
    seek: 'setposition',
    status: 'status',
    volume: 'volume'
}

export {OPTIONS, STATE, CONTROLS, DBUS}
