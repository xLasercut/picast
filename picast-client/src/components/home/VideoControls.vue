<template>
  <v-layout justify-center wrap>
    <v-flex xs12 class="text-xs-center">
      <control-btn color="primary" :disabled="disabled" @click="play()">mdi-play</control-btn>
      <control-btn color="warning" :disabled="disabled" @click="pause()">mdi-pause</control-btn>
      <control-btn color="error" :disabled="disabled" @click="stop()">mdi-stop</control-btn>
      <control-btn color="primary" :disabled="disabled">mdi-skip-previous</control-btn>
      <control-btn color="primary" :disabled="disabled">mdi-skip-next</control-btn>
    </v-flex>
  </v-layout>
</template>

<script lang="coffee">
  import ControlBtn from './ControlBtn.vue'

  export default
    components: { ControlBtn }
    computed:
      disabled: () ->
        return !this.$store.state.connected
    methods:
      stop: () ->
        this.$socket.emit('STOP_VIDEO')
      pause: () ->
        this.$socket.emit 'PLAYER_STATUS', null, (callback) =>
          console.log(callback)
      play: () ->
        this.$socket.emit 'PLAYER_VOLUME', null, (callback) =>
          console.log(callback)
</script>