import EventBus from './event-bus.coffee'

export default
  methods:
    notifySuccess: (msg) ->
      EventBus.$emit('app-notification', 'success', msg)
    notifyError: (msg) ->
      EventBus.$emit('app-notification', 'error', msg)
    notifyWarning: (msg) ->
      EventBus.$emit('app-notification', 'warning', msg)