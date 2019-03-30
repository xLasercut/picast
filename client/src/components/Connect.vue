<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="8">
            <el-input v-model.trim="host" clearable>
                <template slot="prepend">Host</template>
            </el-input>
        </el-col>
        <el-col :span="8">
            <el-input v-model.trim="port" maxlength="4" clearable>
                <template slot="prepend" >Port</template>
            </el-input>
        </el-col>
        <el-col :span="4">
            <el-button
                @click="checkConnection()"
                type="primary"
            >Connect</el-button>
        </el-col>
    </el-row>
</template>

<script lang="coffee">
    import axios from 'axios'
    import Notification from '@/mixins/notification.coffee'

    export default
        mixins: [ Notification ]
        data: () ->
            host: env.REQUEST_HOST,
            port: 8000,
            loading: ''
        methods:
            checkConnection: () ->
                this.loading = this.$loading()
                this.$store.commit('setBaseUrl', "http://#{this.host}:#{this.port}")
                body = { status: [] }
                axios.post(this.$store.getters.statusUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess('Connected to raspberry pi')
                    this.$store.commit('enableVidControl')
                .catch (e) =>
                    this.loading.close()
                    this.notifyError('Unable to connect to raspberry pi')
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }
</style>
