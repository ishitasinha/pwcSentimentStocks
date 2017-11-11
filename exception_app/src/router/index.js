import Vue from 'vue'
import Router from 'vue-router'
import Senti from '@/components/Senti'
import Vuetify from 'vuetify'
import VueCharts from 'vue-chartjs'
import('/home/reaper/Documents/H2I/pwcSentimentStocks/exception_app/node_modules/vuetify/dist/vuetify.min.css') // Ensure you are using css-loader

Vue.use(Vuetify)
Vue.use(VueCharts)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Senti',
      component: Senti
    }
  ]
})
