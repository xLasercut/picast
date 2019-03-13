<template>
    <el-row>
        <el-col :span="4">
            <el-button 
                :disabled="$store.state.disabled"
                @click="toggleMute()"
            ><font-awesome-icon :icon="volumeIcon()"/></el-button>
        </el-col>
        <el-col :span="20">
            <el-slider
                v-model="volume"
                :disabled="$store.state.disabled"
                :min="0"
                :max="10"
                @change="setVolume()"
                show-input
            ></el-slider>
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
                    return "volume-mute"
                }
                else if (this.volume == 0) {
                    return "volume-off"
                }
                else if (this.volume < 5) {
                    return "volume-down"
                }
                else {
                    return "volume-up"
                }
            },
            toggleMute() {
                if (this.muted) {
                    this.controlCommand("unmute")
                    .then((res) => {
                        this.muted = false
                    })
                    .catch((e) => {
                        this.notifyError(e.response.data)
                    })
                }

                this.controlCommand("mute")
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

                })
                .catch((e) => {
                    this.notifyError(e.response.data)
                })
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
