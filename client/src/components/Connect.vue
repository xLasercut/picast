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
            <el-button @click="checkConnection()" type="primary">Connect</el-button>
        </el-col>
    </el-row>
</template>

<script>
    import axios from 'axios'
    import NotificationHelper from '@/mixins/notification-helper.js'

    export default {
        data() {
            return {
                port: 8001,
                host: ''
            }
        },
        mixins: [
            NotificationHelper
        ],
        methods: {
            checkConnection() {
                axios.get(`${this.baseUrl()}/status`)
                .then(response => {
                    this.$store.commit('setDisableControl', false)
                    this.$store.commit('setBaseUrl', this.baseUrl())
                    this.notifySuccess('Connected to picast server')
                })
                .catch(error => {
                    this.notifyError('Could not connect to picast server')
                })

            },
            baseUrl() {
                return `http://${this.host}:${this.port}`
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
