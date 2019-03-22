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
    import ApiConnector from '@/mixins/api-connector.coffee'
    export default
        mixins: [ 
            ApiConnector
        ]
        data: () ->
            host: env.REQUEST_HOST,
            port: 8000
        methods:
            checkConnection: () ->
                this.$emit('loadingTrue')
                this.$store.commit('setBaseUrl', "http://#{this.host}:#{this.port}")
                this.getVideoStats([])
                .then (res) =>
                    this.notifySuccess('Connected to raspberry pi')
                    this.$store.commit('enableVidControl')
                    this.$emit('loadingFalse')
                .catch (e) =>
                    this.notifyError('Unable to connect to raspberry pi')
                    this.$emit('loadingFalse')
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-bottom: 50px;
    }
</style>