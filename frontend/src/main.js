import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import $ from "jquery";

window.$ = $;

import {globalMixin} from './global_mixins'


Vue.config.productionTip = false
Vue.mixin(globalMixin)

new Vue({
    render: h => h(App),
}).$mount('#app')
