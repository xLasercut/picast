<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="10">
                <video-input></video-input>
                <video-seek-bar></video-seek-bar>
                <video-controls></video-controls>
                <video-volume></video-volume>
            </v-col>
        </v-row>
    </v-container>
</template>

<script type="ts">
    import {createComponent} from '@vue/composition-api'
    import VideoInput from '@/home/VideoInput.vue'
    import VideoControls from '@/home/VideoControls.vue'
    import VideoSeekBar from '@/home/VideoSeekBar.vue'
    import VideoVolume from '@/home/VideoVolume.vue'

    export default createComponent({
        components: {
            VideoInput,
            VideoControls,
            VideoSeekBar,
            VideoVolume
        }
    })
</script>
