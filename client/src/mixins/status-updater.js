export default {
    methods: {
        pauseUpdate() {
            this.$store.commit('setPauseUpdate', true)
        },
        unpauseUpdate() {
            this.$store.commit('setPauseUpdate', false)
        },
        playbackTrue() {
            this.$store.commit('setPlaybackStatus', true)
        },
        playbackFalse() {
            this.$store.commit('setPlaybackStatus', false)
        }
    }
}