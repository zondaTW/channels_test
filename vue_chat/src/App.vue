<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view
      room-name="test"
    />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 60px;
}
</style>
