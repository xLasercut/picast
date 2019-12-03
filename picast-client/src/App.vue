<template>
    <v-app>
        <app-notification></app-notification>
        <nav-bar></nav-bar>
        <router-view></router-view>
    </v-app>
</template>

<script lang="ts">
    import {createComponent} from '@vue/composition-api'
    import AppNotification from '@/app/AppNotification.vue'
    import NavBar from '@/app/NavBar.vue'

    export default createComponent({
        components: {
            AppNotification,
            NavBar
        }
    })
</script>
