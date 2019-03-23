<template>
    <el-row :gutter="10" type="flex" justify="center">
        <el-col :span="3">
            <el-button 
                :disabled="$store.getters.canControl"
                @click="toggleMute()"
            ><font-awesome-icon :icon="volumeIcon()"/></el-button>
        </el-col>
        <el-col :span="8">
            <div @mousedown="$store.commit('pauseUpdate')">
                <el-slider
                    v-model="volume"
                    :disabled="$store.getters.canControl"
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
    import Notification from '@/mixins/notification.coffee'
    import axios from 'axios'

    export default
        props: ['value']
        mixins: [ Notification ]
        data: () ->
            volume: this.value,
            muted: false,
            loading: ''
        watch:
            value: (val) ->
                this.volume = val
            volume: (val) ->
                this.$emit('input', val)
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
                this.loading = this.$loading()
                body = {
                    volume: this.volume
                }
                axios.post(this.$store.getters.volumeUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess(res.data)
                .catch (e) =>
                    this.loading.close()
                    this.notifyError(e.response.data)

            toggleMute: () ->
                this.loading = this.$loading()
                if this.muted
                    option = 'unmute'
                else
                    option = 'mute'
                body = { option: option }
                axios.post(this.$store.getters.controlUrl, body)
                .then (res) =>
                    this.loading.close()
                    this.notifySuccess(res.data)
                    this.muted = !this.muted
                .catch (e) =>
                    this.loading.close()
                    this.notifyError(e.response.data)

</script>

<style scoped>
    .el-row {
        margin: 20px;
    }
</style>