<template>
  <v-layout justify-center wrap>
    <v-flex xs10>
      <v-text-field
        v-model.trim="url" box
        label="Video URL"
        append-icon="mdi-send"
      ></v-text-field>
    </v-flex>
  </v-layout>
</template>

<script lang="coffee">
  export default
    data: () ->
      url: ''

</script>