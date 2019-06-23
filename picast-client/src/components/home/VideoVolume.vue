<template>
  <v-layout justify-center wrap>
    <v-flex xs8>
      <v-slider
        v-model.number="volume"
        :prepend-icon="icon"
      ></v-slider>
    </v-flex>
  </v-layout>
</template>


<script lang="coffee">
  export default
    data: () ->
      volume: 50
    computed:
      icon: () ->
        if this.volume > 75
          return 'mdi-volume-high'
        else if this.volume > 50
          return 'mdi-volume-medium'
        return 'mdi-volume-low'
</script>