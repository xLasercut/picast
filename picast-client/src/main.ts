import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueSocketIOExt from 'vue-socket.io-extended'
import io from 'socket.io-client'
import VueCompositionApi from '@vue/composition-api'


Vue.config.productionTip = false

Vue.use(VueCompositionApi)

let options = {
    autoConnect: false
}

// @ts-ignore
Vue.use(VueSocketIOExt, io(PICAST_SERVER, {options}), {store})

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app')
