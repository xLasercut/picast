import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    connected: false,
    dark: false
  },
  mutations: {
    connect(state) {
      state.connected = true
    },
    disconnect(state) {
      state.connected = false
    },
    toggle_theme(state) {
      state.dark = !state.dark
    }
  },
  actions: {

  }
})
