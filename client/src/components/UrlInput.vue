<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="16">
            <el-input :disabled="$store.state.disableControl" v-model.trim="videoUrl" clearable></el-input>
        </el-col>
        <el-col :span="4">
            <el-button :disabled="$store.state.disableControl" @click="sendVideoUrl()">Play Video</el-button>
        </el-col>
    </el-row>
</template>

<script>
    import axios from 'axios'
    import NotificationHelper from '@/mixins/notification-helper.js'
    import StatusUpdater from '@/mixins/status-updater.js'

    export default {
        data () {
            return {
                videoUrl: ''
            }
        },
        mixins: [
            NotificationHelper,
            StatusUpdater
        ],
        methods: {
            sendVideoUrl() {
                axios.post(this.$store.getters.streamUrl, {'url': this.videoUrl})
                .then((response) => {
                    console.log(response)
                    this.playbackTrue()
                })
                .catch((error) => {
                    this.notifyError(error.response.data)
                    this.playbackFalse()
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
