<template>
    <el-row>
        <el-col :span="19">
            <el-slider v-model="videoPosition" :disabled="$store.state.disabled"></el-slider>
        </el-col>
        <el-col :span="5" class="videoTime">
            {{numHours(videoPosition)}}:{{numMinutes(videoPosition)}}:{{numSeconds(videoPosition)}}/{{numHours(videoLength)}}:{{numMinutes(videoLength)}}:{{numSeconds(videoLength)}}
        </el-col>
    </el-row>
</template>

<script>
    export default {
        props: ["disabled"],
        data () {
            return {
                videoPosition: 0,
                videoLength: 0
            }
        },
        methods: {
            numHours(time) {
                var hours = Math.floor(time/3600)
                return this.formatTime(hours)
            },
            numMinutes(time) {
                var minutes = Math.floor(time/60)
                return this.formatTime(minutes)
            },
            numSeconds(time) {
                var seconds = time % 60
                return this.formatTime(seconds)
            },
            formatTime(time) {
                if (time < 10) {
                    return `0${time}`
                }
                return time
            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin: 20px;
        margin-left: 30px;
    }

    .videoTime {
        line-height: 38px;
    }
</style>
