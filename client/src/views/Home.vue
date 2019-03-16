<template>
    <el-main class="home">
        <connect @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></connect>
        <url-input @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></url-input>
        <video-slider @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></video-slider>
        <control-buttons @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></control-buttons>
        <volume-buttons @loadingTrue="loadingTrue()" @loadingFalse="loadingFalse()"></volume-buttons>
    </el-main>
</template>

<script>
    import Connect from '@/components/Connect.vue'
    import UrlInput from '@/components/UrlInput.vue'
    import VideoSlider from '@/components/VideoSlider.vue'
    import ControlButtons from '@/components/ControlButtons.vue'
    import VolumeButtons from '@/components/VolumeButtons.vue'

    export default {
        components: {
            Connect,
            UrlInput,
            VideoSlider,
            ControlButtons,
            VolumeButtons
        },
        data() {
            return {
                loading: ''
            }
        },
        methods: {
            loadingTrue() {
                this.loading = this.$loading()
            },
            loadingFalse() {
                this.loading.close()
            }
        }
    }
</script>

<style>

</style>
