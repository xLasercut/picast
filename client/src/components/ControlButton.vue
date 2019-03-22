<template>
    <el-row>
        <el-button-group>
            <el-button
                :disabled="$store.state.disabled"
                @click="playbackControl('play')"
                type="primary"
            >
                <font-awesome-icon icon="play"/>
            </el-button>
            <el-button
                :disabled="$store.state.disabled"
                @click="playbackControl('pause')"
                type="primary"
            >
                <font-awesome-icon icon="pause"/>
            </el-button>
            <el-button
                :disabled="$store.state.disabled"
                @click="playbackControl('stop')"
                type="danger"
            >
                <font-awesome-icon icon="stop"/>
            </el-button>
            <el-button
                :disabled="$store.state.disabled"
                @click="seekCommand(-30, 'relative')"
                type="warning"
            >
                <font-awesome-icon icon="step-backward"/>
            </el-button>
            <el-button
                :disabled="$store.state.disabled"
                @click="seekCommand(30, 'relative')"
                type="warning"
            >
                <font-awesome-icon icon="step-forward"/>
            </el-button>
        </el-button-group>
    </el-row>
</template>

<script lang="coffee">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import ApiConnector from '@/mixins/api-connector.coffee'

    export default
        components: {
            FontAwesomeIcon
        }
        mixins: [
            ApiConnector
        ]
        methods:
            playbackControl: (command) ->
                this.controlCommand(command)
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }
</style>
