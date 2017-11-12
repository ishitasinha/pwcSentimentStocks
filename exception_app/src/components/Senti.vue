<template>
  <div class="senti">
    <body>
      <div>
        <v-toolbar>
          <v-toolbar-title>{{ title }}</v-toolbar-title>
        </v-toolbar>
      </div>
      <div class="small">
        <line-chart :chart-data="datacollection"></line-chart>
        <v-btn v-on:click="fillData()">Randomize</v-btn>
      </div>
    </body>
  </div>
</template>

<script>
import LineChart from './LineChart.js'
export default {
  components: {
    'line-chart': LineChart
  },
  data () {
    return {
      title: 'Exception App',
      datacollection: null
    }
  },
  mounted () {
  },
  methods: {
    fillData () {
      this.datacollection = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt(),
              this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    },
    changeTitle () {
      this.title = 'Damn!'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.small {
    max-width: 600px;
    margin:  150px auto;
}
</style>
