<template>
    <v-snackbar>
        {{text}}
        <v-btn @click="show=false">
            <v-icon>mdi-close</v-icon>
        </v-btn>
    </v-snackbar>
</template>

<script lang="ts">
    import {createComponent, onMounted, reactive, toRefs} from '@vue/composition-api'
    import {EventBus} from '@/assets/notifications'


    export default createComponent({
        setup(_props, _context) {
            const state = reactive({
                show: false,
                color: '',
                text: ''
            })

            function showNotification(color: string, text: string): void {
                state.color = color
                state.text = text
                state.show = true
            }

            onMounted((): void => {
                EventBus.$on('app-notification', (color: string, text: string) => {
                    if (state.show) {
                        state.show = false
                        setTimeout((): void => {
                            showNotification(color, text)
                        }, 500)
                    }
                    else {
                        showNotification(color, text)
                    }
                })
            })

            return {...toRefs(state)}
        }
    })
</script>
