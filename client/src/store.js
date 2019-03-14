import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        disableControl: true,
        baseUrl: '',
        playbackStatus: true,
        pauseUpdate: false
    },
    mutations: {
        setDisableControl(state, status) {
            state.disableControl = status
        },
        setBaseUrl(state, url) {
            state.baseUrl = url
        },
        setPlaybackStatus(state, status) {
            state.playbackStatus = status
        },
        setPauseUpdate(state, status) {
            state.pauseUpdate = status
        }
    },
    getters: {
        streamUrl: (state) => {
            return `${state.baseUrl}/stream`
        },
        volumeUrl: (state) => {
            return `${state.baseUrl}/volume`
        },
        seekUrl: (state) => {
            return `${state.baseUrl}/seek`
        },
        controlUrl: (state) => {
            return `${state.baseUrl}/control`
        },
        statusUrl: (state) => {
            return `${state.baseUrl}/status`
        },
        canUpdateStatus: (state) => {
            return (state.playbackStatus && !state.disableControl && !state.pauseUpdate)
        }
    },
    actions: {

    }
})
