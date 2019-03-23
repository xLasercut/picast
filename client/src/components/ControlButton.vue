<template>
    <el-row>
        <el-button-group>
            <el-button
                :disabled="$store.getters.canControl"
                @click="playbackControl('play')"
                type="primary"
            >
                <font-awesome-icon icon="play"/>
            </el-button>
            <el-button
                :disabled="$store.getters.canControl"
                @click="playbackControl('pause')"
                type="primary"
            >
                <font-awesome-icon icon="pause"/>
            </el-button>
            <el-button
                :disabled="$store.getters.canControl"
                @click="playbackControl('stop')"
                type="danger"
            >
                <font-awesome-icon icon="stop"/>
            </el-button>
            <el-button
                :disabled="$store.getters.canControl"
                @click="stepTime(-30)"
                type="warning"
            >
                <font-awesome-icon icon="step-backward"/>
            </el-button>
            <el-button
                :disabled="$store.getters.canControl"
                @click="stepTime(30)"
                type="warning"
            >
                <font-awesome-icon icon="step-forward"/>
            </el-button>
        </el-button-group>
    </el-row>
</template>

<script lang="coffee">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import axios from 'axios'
    import Notification from '@/mixins/notification.coffee'

    export default
        components: {
            FontAwesomeIcon
        }
        mixins: [ Notification ]
        data: () ->
            loading: ''
        methods:
            playbackControl: (command) ->
                this.loading = this.$loading()
                body = { option: command }
                axios.post(this.$store.getters.controlUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess(res.data)
                    if command == 'stop'
                        this.$store.commit('disablePlayback')
                .catch (e) =>
                    this.loading.close()
                    this.notifyError(e.response.data)

            stepTime: (time) ->
                this.loading = this.$loading()
                body = {
                    time: time,
                    option: 'relative'
                }
                axios.post(this.$store.getters.seekUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess(res.data)
                .catch (e) =>
                    this.loading.close()
                    this.notifyError(e.response.data)

</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }
</style>
