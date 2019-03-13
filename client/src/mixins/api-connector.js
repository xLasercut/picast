import axios from 'axios'
import NotificationHelper from '@/mixins/notification-helper.js'

export default {
    mixins: [
        NotificationHelper
    ],
    methods: {
        controlCommand(command) {
            var body = {
                "option": command
            }
            return axios.post(this.$store.getters.controlUrl, body)
        },
        seekCommand(time, option) {
            var body = {
                "time": time,
                "option": option
            }
            return axios.post(this.$store.getters.seekUrl, body)
        },
        volumeCommand(volume) {
            var body = {
                "volume": volume
            }
            return axios.post(this.$store.getters.volumeUrl, body)
        }
    }
}
