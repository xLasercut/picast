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

<style>
    .v-application {
        background-color: var(--v-background-base) !important;
    }

    .v-sheet {
        background-color: var(--v-background-darken1) !important;
    }

    .v-slider__thumb-container {
        cursor: pointer;
    }
</style>
