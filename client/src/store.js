import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        disabled: true,
        baseUrl: '',
        playback: false,
        paused: false
    },
    mutations: {
        disableVidControl(state) {
            state.disabled = true
        },
        enableVidControl(state) {
            state.disabled = false
        },
        enablePlayback(state) {
            state.playback = true
        },
        disablePlayback(state) {
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
    actions: {

    },
    getters: {
        canUpdate: (state) => {
            return !state.disabled && state.playback && !state.paused
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
        streamUrl: (state) => {
            return `${state.baseUrl}/stream`
        },
        statusUrl: (state) => {
            return `${state.baseUrl}/status`
        }
    }
})
