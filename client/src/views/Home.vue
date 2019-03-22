<template>
    <div class="home">
        <connect @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></connect>
        <video-url @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></video-url>
        <video-slider @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></video-slider>
        <control-button @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></control-button>
        <volume @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></volume>
    </div>
</template>

<script lang="coffee">
    import Connect from '@/components/Connect.vue'
    import ControlButton from '@/components/ControlButton.vue'
    import VideoUrl from '@/components/VideoUrl.vue'
    import VideoSlider from '@/components/VideoSlider.vue'
    import Volume from '@/components/Volume.vue'

    export default
        name: 'home'
        components: {
            Connect,
            ControlButton,
            VideoUrl,
            VideoSlider,
            Volume
        }
        data: () ->
            loading: ''
        methods:
            loadingTrue: () ->
                this.loading = this.$loading()
            loadingFalse: () ->
                this.loading.close()
</script>
