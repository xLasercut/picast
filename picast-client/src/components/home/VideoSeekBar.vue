<template>
  <v-layout wrap justify-center>
    <v-flex xs8>
      <v-slider v-model.number="position"></v-slider>
    </v-flex>
    <v-flex shrink>
      <div class="video-time">
        {{position}}/{{length}}
      </div>
    </v-flex>
  </v-layout>
</template>

<script lang="coffee">
  export default
    data: () ->
      position: 0
      length: 100
</script>

<style scoped>
  .video-time {
    line-height: 65px;
    height: 100%;
  }
</style>