<template>
    <el-row>
        <el-col :span="19">
            <el-slider
                v-model="videoPosition"
                :disabled="$store.state.disabled"
                :min="0"
                :max="100"
                :format-tooltip="convertToHHMMSS"
                @change="seekCommand(videoPosition, 'absolute')"
            ></el-slider>
        </el-col>
        <el-col :span="5" class="videoTime">
            {{convertToHHMMSS(videoPosition)}}/{{convertToHHMMSS(videoLength)}}
        </el-col>
    </el-row>
</template>

<script>
    import axios from 'axios'
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
                var seconds = time % 60
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
            getVideoStats() {
                if (this.$store.state.playbackStatus) {
                    axios.post(this.$store.getters.statusUrl, {"status": ["length", "position"]})
                    .then((response) => {
                        console.log(response)
                    })
                    .catch((e) => {
                        console.log(e.response.data)
                        if (e.response.status === 403) {
                            this.$store.commit("togglePlaybackStatus", false)
                        }
                    })
                }
            }
        },
        mounted() {
            setInterval(() => {
                this.getVideoStats()
            }, 1000)
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-left: 30px;
    }

    .videoTime {
        line-height: 38px;
    }
</style>
