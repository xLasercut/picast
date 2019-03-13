import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        disabled: true,
        baseUrl: "",
        playbackStatus: false
    },
    mutations: {
        toggleControl(state, status) {
            state.disabled = status
        },
        setBaseUrl(state, url) {
            state.baseUrl = url
        },
        togglePlaybackStatus(state, status) {
            state.playbackStatus = status
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
        }
    },
    actions: {

    }
})
