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
                    :max="2"
                    :step="0.2"
                    :format-tooltip="convertToWhole"
                    @change="setVolume()"
                ></el-slider>
            </div>
        </el-col>
    </el-row>
</template>

<script>
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import ApiConnector from '@/mixins/api-connector.js'

    export default {
        components: {
            FontAwesomeIcon
        },
        mixins: [
            ApiConnector
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
                this.$emit('loadingTrue')
                if (this.muted) {
                    this.controlCommand('unmute')
                    .then((res) => {
                        this.muted = false
                        this.notifySuccess(res.data)
                        this.$emit('loadingFalse')
                    })
                    .catch((e) => {
                        this.notifyError(e.response.data)
                        this.$emit('loadingFalse')
                    })
                } 
                else {
                    this.controlCommand('mute')
                    .then((res) => {
                        this.muted = true
                        this.notifySuccess(res.data)
                        this.$emit('loadingFalse')
                    })
                    .catch((e) => {
                        this.notifyError(e.response.data)
                        this.$emit('loadingFalse')
                    })
                }                
            },
            setVolume() {
                this.volumeCommand(this.volume)
            },
            convertToWhole(volume) {
                return Math.ceil(volume/0.2)
            },
            updateVolumeStats() {
                if (this.$store.getters.canUpdateStatus) {
                    this.getVideoStats(['volume'])
                    .then((res) => {
                        this.volume = res.data.volume
                    })
                    .catch((e) => {
                        console.log(e.response.data)
                        var statusCode = e.response.status
                        var errorMsg = e.response.data

                        if (statusCode === 403 && errorMsg === 'Cannot retrieve stats when no video is playing') {
                            this.$store.commit('playbackFalse')
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
