import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        disabled: true,
        baseUrl: '',
        playback: true,
        paused: false
    },
    mutations: {
        disableVidControl(state) {
            state.disabled = true
        },
        enableVidControl(state) {
            state.disabled = false
        },
        playbackTrue(state) {
            state.playback = true
        },
        playbackFalse(state) {
            state.playback = false
        },
        pauseUpdate(state) {
            state.paused = true
        },
        unpauseUpdate(state) {
            state.paused = false
        },
        setBaseUrl(state, url) {
            state.baseUrl = url
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
            return (state.playback && !state.disabled && !state.paused)
        }
    },
    actions: {

    }
})
