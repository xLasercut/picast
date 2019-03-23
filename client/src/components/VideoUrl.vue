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

<script lang="coffee">
    import axios from 'axios'
    import Notification from '@/mixins/notification.coffee'

    export default
        mixins: [ Notification ]
        data: () ->
            videoUrl: '',
            loading: ''
        methods:
            sendVideoUrl: () ->
                this.loading = this.$loading()
                body = { url: this.videoUrl }
                axios.post(this.$store.getters.streamUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.$store.commit('enablePlayback')
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
