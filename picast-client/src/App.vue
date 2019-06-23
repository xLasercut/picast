<template>
  <v-app :dark="$store.state.dark">
    <app-notification></app-notification>
    <nav-bar></nav-bar>
    <v-container fluid grid-list-lg>
      <router-view></router-view>
    </v-container>
  </v-app>
</template>

<script lang="coffee">
  import AppNotification from './components/shared/AppNotification.vue'
  import Notification from './components/mixins/notification.coffee'
  import NavBar from './components/shared/NavBar.vue'

  export default
    components: { AppNotification, NavBar }
    mixins: [ Notification ]
    sockets:
      connect: () ->
        this.$store.commit('connect')
        this.notifySuccess('Connected to raspberry pi')
      connect_timeout: () ->
        this.$store.commit('disconnect')
        this.notifyError('Cannot connect to raspberry pi')
        this.$socket.disconnect()
      disconnect: () ->
        this.$store.commit('disconnect')
        this.notifyWarning('Disconnected from raspberry pi')
    mounted: () ->
      this.$socket.open()
</script>
