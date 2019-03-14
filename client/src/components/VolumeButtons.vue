<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="3">
            <el-button 
                :disabled="$store.state.disableControl"
                @click="toggleMute()"
            ><font-awesome-icon :icon="volumeIcon()"/></el-button>
        </el-col>
        <el-col :span="8">
            <div @mousedown="pauseUpdate()">
                <el-slider
                    v-model="volume"
                    :disabled="$store.state.disableControl"
                    :min="0"
                    :max="10"
                    @change="setVolume()"
                    show-input
                ></el-slider>
            </div>
        </el-col>
    </el-row>
</template>

<script>
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import ApiConnector from '@/mixins/api-connector.js'
    import StatusUpdater from '@/mixins/status-updater.js'

    export default {
        components: {
            FontAwesomeIcon
        },
        mixins: [
            ApiConnector,
            StatusUpdater
        ],
        data() {
            return {
                volume: 0,
                muted: false
            }
        },
        methods: {
            volumeIcon() {
                if (this.muted) {
                    return 'volume-mute'
                }
                else if (this.volume == 0) {
                    return 'volume-off'
                }
                else if (this.volume < 5) {
                    return 'volume-down'
                }
                else {
                    return 'volume-up'
                }
            },
            toggleMute() {
                if (this.muted) {
                    this.controlCommand('unmute')
                    .then((res) => {
                        this.muted = false
                    })
                    .catch((e) => {
                        this.notifyError(e.response.data)
                    })
                }

                this.controlCommand('mute')
                .then((res) => {
                    this.muted = true
                })
                .catch((e) => {
                    this.notifyError(e.response.data)
                })
            },
            setVolume() {
                this.volumeCommand(this.volume)
                .then((res) => {
                    this.notifySuccess(res.data)
                })
                .catch((e) => {
                    this.notifyError(e.response.data)
                })
            },
            updateVolumeStats() {
                if (this.$store.getters.canUpdateStatus) {
                    this.getVideoStats(['volume'])
                    .then((res) => {

                    })
                    .catch((e) => {
                        console.log(e.response.data)
                        var statusCode = e.response.status
                        var errorMsg = e.response.data

                        if (statusCode === 403 && errorMsg === 'Cannot retrieve stats when no video is playing') {
                            this.playbackFalse()
                        }
                        else {
                            this.notifyError(errorMsg)
                        }
                    })
                }
            }
        },
        mounted() {
            setInterval(() =>{
                this.updateVolumeStats()
            }, 5000)
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
