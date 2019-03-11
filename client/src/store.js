import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        disabled: true,
        baseUrl: ""
    },
    mutations: {
        toggleControl(state, status) {
            state.disabled = status
        }
    },
    actions: {

    }
})
