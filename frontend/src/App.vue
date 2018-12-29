<template>
  <div id="app">
    <Files msg="Files"/>
  </div>
</template>

<script>
import Files from './components/Files.vue'

export default {
  name: 'app',
  components: {
    Files
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
