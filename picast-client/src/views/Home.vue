<template>
  <v-layout justify-center wrap>
    <v-flex xs12>
      <video-input></video-input>
      <video-seek-bar></video-seek-bar>
      <video-controls></video-controls>
      <video-volume></video-volume>
    </v-flex>
  </v-layout>
</template>

<script lang="coffee">
  import VideoInput from '../components/home/VideoInput.vue'
  import VideoSeekBar from '../components/home/VideoSeekBar.vue'
  import VideoControls from '../components/home/VideoControls.vue'
  import VideoVolume from '../components/home/VideoVolume.vue'

  export default
    components: { VideoInput, VideoSeekBar, VideoControls, VideoVolume }

</script>
