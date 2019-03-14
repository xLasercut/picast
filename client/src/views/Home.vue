<template>
    <el-main class="home">
        <connect></connect>
        <url-input></url-input>
        <video-slider></video-slider>
        <control-buttons></control-buttons>
        <volume-buttons></volume-buttons>
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
        }
    }
</script>

<style>

</style>
