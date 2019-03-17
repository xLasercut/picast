<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="16">
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
                videoUrl: ''
            }
        },
        mixins: [
            NotificationHelper
        ],
        methods: {
            sendVideoUrl() {
                this.$emit('loadingTrue')
                axios.post(this.$store.getters.streamUrl, {'url': this.videoUrl})
                .then((res) => {
                    this.notifySuccess(res.data)
                    this.$store.commit('playbackTrue')
                    this.$emit('loadingFalse')
                })
                .catch((error) => {
                    this.notifyError(error.response.data)
                    this.$store.commit('playbackFalse')
                    this.$emit('loadingFalse')
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
