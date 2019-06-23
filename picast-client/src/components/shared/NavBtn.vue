<template>
  <v-btn @click="$emit('click')" :color="color" v-on="activator" flat :disabled="disabled" :id="id">
    <slot></slot>
    <v-icon right>
      {{icon}}
    </v-icon>
  </v-btn>
</template>

<script lang="coffee">
  export default
    props: [ 'color', 'icon', 'disabled', 'activator', 'id' ]
</script>