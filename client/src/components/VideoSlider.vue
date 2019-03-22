<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="15">
            <div class="sliderContainer" @mousedown="$store.commit('pauseUpdate')">
                <el-slider
                    v-model="videoPosition"
                    :disabled="$store.state.disabled"
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
    import ApiConnector from '@/mixins/api-connector.coffee'

    export default
        mixins: [
            ApiConnector
        ]
        data: () ->
            videoPosition: 600,
            videoLength: 0
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
            updateVideoStats: () ->
                if this.$store.getters.canUpdate
                    this.getVideoStats(['length', 'position'])
                    .then (res) =>
                        this.videoPosition = res.data.position
                        this.videoLength = res.data.length
                    .catch (e) =>
                        statusCode = e.response.status
                        errorMsg = e.response.data

                        if statusCode == 403 && errorMsg == 'Cannot retrieve stats when no video is playing'
                            this.$store.commit('disablePlayback')
                        else
                            this.notifyError(errorMsg)
            setPosition: () ->
                this.seekCommand(this.videoPosition, 'absolute')
        mounted: () ->
            setInterval(() =>
                this.updateVideoStats()
            , 5000)
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