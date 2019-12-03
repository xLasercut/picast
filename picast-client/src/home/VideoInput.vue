<template>
    <v-row justify="center">
        <v-col cols="12">
            <v-text-field
                filled v-model.trim="url"
                label="Video URL" append-icon="mdi-send"
                @click:append="playVideo()"
            ></v-text-field>
        </v-col>
    </v-row>
</template>

<script lang="ts">
    import {createComponent, reactive, toRefs} from '@vue/composition-api'

    export default createComponent({
        setup(_props, context) {
            const state = reactive({
                url: ''
            })

            function playVideo(): void {
                console.log('test')
                context.root.$socket.client.emit('PLAY_VIDEO', state.url)
            }

            return {...toRefs(state), playVideo}
        }
    })
</script>
