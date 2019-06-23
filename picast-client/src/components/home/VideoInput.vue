<template>
  <v-layout justify-center wrap>
    <v-flex xs10>
      <v-text-field
        v-model.trim="url" box
        label="Video URL"
        append-icon="mdi-send"
        @click:append="playVideo()"
      ></v-text-field>
    </v-flex>
  </v-layout>
</template>

<script lang="coffee">
  export default
    data: () ->
      url: ''
    methods:
      playVideo: () ->
        this.$socket.emit('PLAY_VIDEO', this.url)
</script>