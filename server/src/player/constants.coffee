options = [ '-o hdmi' ]

state = {
  playing: 0,
  paused: 1,
  idle: 2
}

controls = {
  stop: 'q',
  pause: 'p'
}

dbus = {
  seek: 'setposition',
  status: 'status',
  volume: 'volume'
}

module.exports = {
  options,
  state,
  controls,
  dbus
}