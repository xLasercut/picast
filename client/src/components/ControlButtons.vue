<template>
    <el-row>
        <el-button
            :disabled="$store.state.disableControl"
            @click="playbackControl('play')"
            type="primary"
        >
            <font-awesome-icon icon="play"/>
        </el-button>
        <el-button
            :disabled="$store.state.disableControl"
            @click="playbackControl('pause')"
            type="primary"
        >
            <font-awesome-icon icon="pause"/>
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
                    this.notifySuccess(res.data)
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
        margin-bottom: 50px;
    }
</style>
