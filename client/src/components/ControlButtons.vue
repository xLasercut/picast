<template>
    <el-row>
        <el-button
            :disabled="$store.state.disableControl"
            @click="playpauseVideo()"
            type="primary"
        >
            <font-awesome-icon :icon="playbackStatus"/>
        </el-button>
        <el-button
            :disabled="$store.state.disableControl"
            @click="playbackControl('stop')"
            type="danger"
        >
            <font-awesome-icon icon="stop"/>
        </el-button>
        <el-button
            :disabled="$store.state.disableControl"
            @click="stepPosition(-30)"
            type="warning"
        >
            <font-awesome-icon icon="step-backward"/>
        </el-button>
        <el-button
            :disabled="$store.state.disableControl"
            @click="stepPosition(30)"
            type="warning"
        >
            <font-awesome-icon icon="step-forward"/>
        </el-button>
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
                playbackStatus: 'play'
            }
        },
        methods: {
            playbackControl(command) {
                this.controlCommand(command)
                .then((res) => {
                    this.notifySuccess(res.data)
                })
                .catch((e) => {
                    this.notifyError(e.response.data)
                })
            },
            stepPosition(time) {
                this.seekCommand(time, 'relative')
                .then((res) => {

                })
                .catch((e) => {
                    this.notifyError(e.response.data)
                })
            },
            playpauseVideo() {
                if (this.playbackStatus === 'play') {
                    var command = 'pause'
                }
                else {
                    var command = 'play'
                }
                this.controlCommand(command)
                .then((res) => {
                    this.playbackStatus = command
                })
                .cat((e) => {
                    this.notifyError(e.response.data)
                })
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }
</style>
