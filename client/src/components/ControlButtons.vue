<template>
    <el-row>
        <el-button :disabled="$store.state.disabled"><font-awesome-icon :icon="playbackStatus"/></el-button>
        <el-button :disabled="$store.state.disabled"><font-awesome-icon icon="stop"/></el-button>
        <el-button :disabled="$store.state.disabled"><font-awesome-icon icon="step-backward"/></el-button>
        <el-button :disabled="$store.state.disabled"><font-awesome-icon icon="step-forward"/></el-button>
    </el-row>
</template>

<script>
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

    export default {
        props: ["disabled"],
        components: {
            FontAwesomeIcon
        },
        data() {
            return {
                playbackStatus: "play"
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
