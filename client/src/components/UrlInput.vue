<template>
    <el-row>
        <el-input :disabled="$store.state.disabled">
            <el-button slot="append" :disabled="$store.state.disabled">Play Video</el-button>
        </el-input>
    </el-row>
</template>

<script>
    export default {
        props: ["disabled", "value"],
        data () {
            return {
                disableControl: this.disabled
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
