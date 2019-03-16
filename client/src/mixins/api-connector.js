import axios from 'axios'
import NotificationHelper from '@/mixins/notification-helper.js'

export default {
    mixins: [
        NotificationHelper
    ],
    methods: {
        controlCommand(command) {
            var body = {
                'option': command
            }
            return axios.post(this.$store.getters.controlUrl, body, {'timeout': 5000})
        },
        seekCommand(time, option) {
            this.$emit('loadingTrue')
            var body = {
                'time': time,
                'option': option
            }
            axios.post(this.$store.getters.seekUrl, body)
            .then((res) => {
                this.notifySuccess(res.data)
                this.$emit('loadingFalse')
            })
            .catch((e) => {
                this.notifyError(e.response.data)
                this.$emit('loadingFalse')
            })
        },
        volumeCommand(volume) {
            this.$emit('loadingTrue')
            var body = {
                'volume': volume
            }
            axios.post(this.$store.getters.volumeUrl, body)
            .then((res) => {
                this.notifySuccess(res.data)
                this.$emit('loadingFalse')
            })
            .catch((e) => {
                this.notifyError(e.response.data)
                this.$emit('loadingFalse')
            })
        },
        getVideoStats(stats) {
            var body = {
                'status': stats
            }
            return axios.post(this.$store.getters.statusUrl, body)
        }
    }
}
