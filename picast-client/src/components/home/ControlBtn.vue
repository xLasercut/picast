<template>
  <v-btn depressed :color="color" :disabled="disabled">
    <v-icon>
      <slot></slot>
    </v-icon>
  </v-btn>
</template>

<script lang="coffee">
  export default
    props: [ 'color', 'disabled' ]
</script>