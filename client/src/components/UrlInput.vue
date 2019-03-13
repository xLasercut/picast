<template>
    <el-row>
        <el-col :span="20">
            <el-input :disabled="$store.state.disabled" v-model.trim="videoUrl" clearable></el-input>
        </el-col>
        <el-col :span="4">
            <el-button :disabled="$store.state.disabled" @click="sendVideoUrl()">Play Video</el-button>
        </el-col>
    </el-row>
</template>

<script>
    import axios from 'axios'
    import NotificationHelper from '@/mixins/notification-helper.js'

    export default {
        data () {
            return {
                videoUrl: ""
            }
        },
        mixins: [NotificationHelper],
        methods: {
            sendVideoUrl() {
                axios.post(this.$store.getters.streamUrl, {"url": this.videoUrl})
                .then((response) => {
                    console.log(response)
                    this.$store.commit("togglePlaybackStatus", true)
                })
                .catch((error) => {
                    this.notifyError(error.response.data)
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
