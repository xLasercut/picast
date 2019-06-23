import Vue from 'vue'
import store from '../store.js'
import VueSocketio from 'vue-socket.io-extended'
import io from 'socket.io-client'

var options = {
  autoConnect: false
}

Vue.use(VueSocketio, io(PICAST_SERVER, options), { store })