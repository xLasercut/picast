<template>
    <div id="app" @mouseup="unpauseUpdate()">
        <router-view></router-view>
    </div>
</template>

<script>
    import StatusUpdater from '@/mixins/status-updater.js'

    export default {
        name: 'app',
        mixins: [
            StatusUpdater
        ]
    }
</script>

<style>
    body {
        font-family: 'Helvetica Neue',Helvetica,'PingFang SC','Hiragino Sans GB','Microsoft YaHei','微软雅黑',Arial,sans-serif;
        height: 100vh;
        width: 100vw;
        margin: 0;
    }

    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        height: 100%;
        width: 100%;
    }
</style>
