<template>
    <v-row justify="center">
        <control-btn color="primary" :disabled="disabled" @click="play()">mdi-play</control-btn>
        <control-btn color="warning" :disabled="disabled" @click="pause()">mdi-pause</control-btn>
        <control-btn color="error" :disabled="disabled" @click="stop()">mdi-stop</control-btn>
        <control-btn color="primary" :disabled="disabled">mdi-skip-previous</control-btn>
        <control-btn color="primary" :disabled="disabled">mdi-skip-next</control-btn>
    </v-row>
</template>

<script lang="ts">
    import {computed, createComponent, reactive} from '@vue/composition-api'
    import ControlBtn from '../components/buttons/ControlBtn.vue'

    export default createComponent({
        components: {
            ControlBtn
        },
        setup(_props, context) {
            const state = reactive({})

            const socket = context.root.$socket

            const disabled = computed((): boolean => {
                return context.root.$store.state.connected
            })

            function play(): void {
                socket.client.emit('PLAY_VIDEO')
            }

            function pause(): void {
                socket.client.emit('PLAY_PAUSE')
            }

            return {disabled}
        }
    })
</script>
