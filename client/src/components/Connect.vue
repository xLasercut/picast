<template>
    <el-row>
        <el-input v-model="picastBase">
            <el-button slot="append" @click="checkConnection()">Connect</el-button>
        </el-input>
    </el-row>
</template>

<script>
    export default {
        data() {
            return {
                picastBase: ""
            }
        },
        methods: {
            checkConnection() {
                this.$store.commit('toggleControl', false)
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
