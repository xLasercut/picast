<template>
    <div class="home">
        <connect></connect>
        <video-url></video-url>
        <video-slider :vidLength="videoLength" v-model="videoPosition"></video-slider>
        <control-button></control-button>
        <volume v-model="volume"></volume>
    </div>
</template>

<script lang="coffee">
    import Connect from '@/components/Connect.vue'
    import ControlButton from '@/components/ControlButton.vue'
    import VideoUrl from '@/components/VideoUrl.vue'
    import VideoSlider from '@/components/VideoSlider.vue'
    import Volume from '@/components/Volume.vue'
    import Notification from '@/mixins/notification.coffee'
    import axios from 'axios'

    export default
        name: 'home'
        mixins: [ Notification ]
        components: {
            Connect,
            ControlButton,
            VideoUrl,
            VideoSlider,
            Volume
        }
        data: () ->
            volume: 0,
            videoLength: 0,
            videoPosition: 0
        methods:
            updateVideoStats: () ->
                if this.$store.getters.canUpdate
                    body = {
                        status: ['length', 'position', 'volume']
                    }
                    axios.post(this.$store.getters.statusUrl, body)
                    .then (res) =>
                        console.log(res.data)
                        this.videoPosition = res.data.position
                        this.videoLength = res.data.length
                        this.volume = res.data.volume
                    .catch (e) =>
                        statusCode = e.response.status
                        errorMsg = e.response.data

                        if statusCode == 403 && errorMsg == 'Cannot retrieve stats when no video is playing'
                            this.$store.commit('disablePlayback')
                        else
                            this.notifyError(errorMsg)
        mounted: () ->
            setInterval(() =>
                this.updateVideoStats()
            , 1000)
</script>
