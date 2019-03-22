<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="3">
            <el-button 
                :disabled="$store.state.disabled"
                @click="toggleMute()"
            ><font-awesome-icon :icon="volumeIcon()"/></el-button>
        </el-col>
        <el-col :span="8">
            <div @mousedown="$store.commit('pauseUpdate')">
                <el-slider
                    v-model="volume"
                    :disabled="$store.state.disabled"
                    :min="0"
                    :max="2"
                    :step="0.2"
                    :format-tooltip="convertToWhole"
                    @change="setVolume()"
                ></el-slider>
            </div>
        </el-col>
    </el-row>
</template>

<script lang="coffee">
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    import ApiConnector from '@/mixins/api-connector.coffee'

    export default
        mixins: [
            ApiConnector
        ]
        data: () ->
            volume: 0.2,
            muted: false
        components: {
            FontAwesomeIcon
        }
        methods:
            volumeIcon: () ->
                if this.muted
                    return 'volume-mute'
                else if this.volume == 0
                    return 'volume-off'
                else if this.volume < 1
                    return 'volume-down'
                else
                    return 'volume-up'
            convertToWhole: (volume) ->
                return Math.ceil(volume/0.2)
            setVolume: () ->
                this.volumeCommand(this.volume)
            toggleMute: () ->
                if this.muted
                    this.controlCommand('mute')
                else
                    this.controlCommand('unmute')
            updateVolumeStats: () ->
                if this.$store.getters.canUpdate
                    this.getVideoStats(['volume'])
                    .then (res) =>
                        this.volume = res.data.volume
                    .catch (e) =>
                        statusCode = e.response.status
                        errorMsg = e.response.data

                        if statusCode == 403 && errorMsg == 'Cannot retrieve stats when no video is playing'
                            this.$store.commit('disablePlayback')
                        else
                            this.notifyError(errorMsg)
        mounted: () ->
            setInterval( () =>
                this.updateVolumeStats()
            , 5000)
</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>