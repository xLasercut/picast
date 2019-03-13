<template>
    <el-row>
        <el-button :disabled="$store.state.disabled" @click="playbackControl('playpause')">
            <font-awesome-icon :icon="playbackStatus"/>
        </el-button>
        <el-button :disabled="$store.state.disabled" @click="playbackControl('stop')">
            <font-awesome-icon icon="stop"/>
        </el-button>
        <el-button :disabled="$store.state.disabled" @click="seekCommand(-30, 'relative')">
            <font-awesome-icon icon="step-backward"/>
        </el-button>
        <el-button :disabled="$store.state.disabled" @click="seekCommand(30, 'relative')">
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
                playbackStatus: "play"
            }
        },
        methods: {
            playbackControl(command) {
                this.controlCommand(command)
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
