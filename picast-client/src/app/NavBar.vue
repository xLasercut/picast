<template>
    <v-toolbar flat height="60px" max-height="60px">
        <v-toolbar-items>
            <nav-btn icon="mdi-theme-light-dark" @click="toggleTheme()"></nav-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <nav-btn icon="mdi-sync" color="warning" @click="connectToPi()"></nav-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script lang="ts">
    import {createComponent} from '@vue/composition-api'
    import NavBtn from '@/components/buttons/NavBtn.vue'

    export default createComponent({
        components: {
            NavBtn
        },
        setup(_props, context) {
            function toggleTheme(): void {
                context.root.$vuetify.theme.dark = !context.root.$vuetify.theme.dark
            }

            function connectToPi(): void {
                console.log('tst')
                context.root.$socket.client.connect()
            }

            return {toggleTheme, connectToPi}
        }
    })
</script>
