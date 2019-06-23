<template>
  <v-toolbar
    flat height="60px"
  >
    <v-toolbar-items>
      <nav-btn icon="mdi-theme-light-dark" @click="$store.commit('toggle_theme')">
        {{themeBtnWord}}
      </nav-btn>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <v-toolbar-items>
      <nav-btn color="warning" icon="mdi-sync" :disabled="$store.state.connected" @click="$socket.open()">
        Reconnect
      </nav-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script lang="coffee">
  import NavBtn from './NavBtn.vue'

  export default
    components: { NavBtn }
    computed:
      themeBtnWord: () ->
        if this.$store.state.dark
          return 'Light'
        return 'Dark'
</script>