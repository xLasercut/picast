<template>
    <el-row>
        <el-col :span="4">
            <el-button :disabled="$store.state.disabled"><font-awesome-icon :icon="volumeIcon()"/></el-button>
        </el-col>
        <el-col :span="20">
            <el-slider v-model="volume" :disabled="$store.state.disabled" show-input></el-slider>
        </el-col>
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
                volume: 0
            }
        },
        methods: {
            volumeIcon() {
                if (this.volume == 0) {
                    return "volume-off"
                }
                else if (this.volume < 50) {
                    return "volume-down"
                }
                else {
                    return "volume-up"
                }
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>
