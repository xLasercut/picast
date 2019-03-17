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

<script>
    import ApiConnector from '@/mixins/api-connector.js'

    export default {
        data () {
            return {
                videoPosition: 0,
                videoLength: 0
            }
        },
        mixins: [
            ApiConnector
        ],
        methods: {
            numHours(time) {
                var hours = Math.floor(time/3600)
                return this.formatTime(hours)
            },
            numMinutes(time) {
                var minutes = Math.floor(time/60)
                return this.formatTime(minutes)
            },
            numSeconds(time) {
                var seconds = Math.floor(time % 60)
                return this.formatTime(seconds)
            },
            formatTime(time) {
                if (time < 10) {
                    return `0${time}`
                }
                return time
            },
            convertToHHMMSS(time) {
                var hours = this.numHours(time)
                var mins = this.numMinutes(time)
                var seconds = this.numSeconds(time)
                return `${hours}:${mins}:${seconds}`
            },
            updateVideoStats() {
                if (this.$store.getters.canUpdateStatus) {
                    this.getVideoStats(['length', 'position'])
                    .then((response) => {
                        var stats = response.data
                        this.videoLength = stats.length
                        this.videoPosition = stats.position
                    })
                    .catch((e) => {
                        console.log(e.response.data)
                        var statusCode = e.response.status
                        var errorMsg = e.response.data

                        if (statusCode === 403 && errorMsg === 'Cannot retrieve stats when no video is playing') {
                            this.$store.commit('playbackFalse')
                            this.videoLength = 0
                            this.videoPosition = 0
                        }
                        else {
                            this.notifyError(errorMsg)
                        }
                    })
                }
            },
            setPosition() {
                this.seekCommand(this.videoPosition, 'absolute')
            }
        },
        mounted() {
            setInterval(() => {
                this.updateVideoStats()
            }, 5000)
        }
    }
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
