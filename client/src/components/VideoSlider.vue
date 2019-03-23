<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="15">
            <div class="sliderContainer" @mousedown="$store.commit('pauseUpdate')">
                <el-slider
                    v-model="videoPosition"
                    :disabled="$store.getters.canControl"
                    :min="0"
                    :max="videoLength"
                    :format-tooltip="convertToHHMMSS"
                    @change="setPosition()"
                ></el-slider>
            </div>
        </el-col>
        <el-col :span="5" class="videoTime">
            {{convertToHHMMSS(videoPosition)}}/{{convertToHHMMSS(videoLength)}}
        </el-col>
    </el-row>
</template>

<script lang="coffee">
    import Notification from '@/mixins/notification.coffee'
    import axios from 'axios'

    export default
        props: ['vidLength', 'value']
        mixins: [ Notification ]
        watch:
            videoPosition: (val) ->
                this.$emit('input', val)
            vidLength: (val) ->
                this.videoLength = val
            value: (val) ->
                this.videoPosition = val
        data: () ->
            videoPosition: this.value,
            videoLength: this.vidLength
            loading: ''
        methods:
            formatTime: (time) ->
                if time < 10
                    return "0#{time}"
                return time
            convertToHHMMSS: (time) ->
                hours = this.formatTime(Math.floor(time/3600))
                minutes = this.formatTime(Math.floor(time/60))
                seconds = this.formatTime(Math.floor(time % 60))
                return "#{hours}:#{minutes}:#{seconds}"
            setPosition: () ->
                this.loading = this.$loading()
                body = {
                    time: this.videoPosition,
                    option: 'absolute'
                }
                axios.post(this.$store.getters.seekUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess(res.data)
                .catch (e) =>
                    this.loading.close()
                    this.notifyError(e.response.data)
                
        
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }

    .videoTime {
        line-height: 38px;
    }
</style>