<template>
    <v-row justify="center">
        <v-col>
            <v-slider v-model.number="currentTime"></v-slider>
        </v-col>
        <v-col cols="auto">
            {{toTimeStamp(currentTime)}}/{{toTimeStamp(maxTime)}}
        </v-col>
    </v-row>
</template>

<script lang="ts">
    import {createComponent, reactive, toRefs} from '@vue/composition-api'

    export default createComponent({
        setup(_props, context) {
            const state = reactive({
                currentTime: 0,
                maxTime: 0
            })

            function toTimeStamp(time: number): string {
                let hours = formatTime(Math.floor(time / 3600))
                let minutes = formatTime(Math.floor(time / 60))
                let seconds = formatTime(Math.floor(time % 60))

                return `${hours}:${minutes}:${seconds}`
            }

            function formatTime(time: number): string {
                if (time < 10) {
                    return `0${time}`
                }
                return `${time}`
            }

            return {...toRefs(state), toTimeStamp}
        }
    })
</script>
