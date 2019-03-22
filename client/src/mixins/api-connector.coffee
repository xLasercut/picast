import axios from 'axios'
import Notification from '@/mixins/notification.coffee'

export default
    mixins: [ 
        Notification
    ]
    methods:
        volumeCommand: (volume) ->
            this.$emit('loadingTrue')
            body = {
                volume: volume
            }
            axios.post(this.$store.getters.volumeUrl, body)
            .then (res) =>
                this.$emit('loadingFalse')
                this.notifySuccess(res.data)
            .catch (e) =>
                this.$emit('loadingFalse')
                this.notifyError(e.response.data)
        seekCommand: (time, option) ->
            this.$emit('loadingTrue')
            body = {
                time: time,
                option: option
            } 
            axios.post(this.$store.getters.seekUrl, body)
            .then (res) =>
                this.$emit('loadingFalse')
                this.notifySuccess(res.data)
            .catch (e) =>
                this.$emit('loadingFalse')
                this.notifyError(e.response.data)
        controlCommand: (command) ->
            this.$emit('loadingTrue')
            body = {
                option: command
            }
            axios.post(this.$store.getters.controlUrl, body)
            .then (res) =>
                this.$emit('loadingFalse')
                this.notifySuccess(res.data)
            .catch (e) =>
                this.$emit('loadingFalse')
                this.notifyError(e.response.data)
        getVideoStats: (stats) ->
            body = {
                status: stats
            }
            return axios.post(this.$store.getters.statusUrl, body)
