<template>
  <div id="homeSection" class="Room container">
    <div class="row h-15">
      <div class="col" >
        <h1><span class="badge badge-primary">Join ?</span></h1>
      </div>
    </div>
    <div class="row h-10">
      <input
        ref="inputField"
        type="text"
        class="w-75"
        v-focus
        placeholder="Room name"
        v-model="inputContent"
      />
      <router-link
        :to="{
          name: 'Room',
          params: {
            roomName: inputContent
          }
        }"
        tag="button"
        class="btn btn-primary w-25"
        :class="{disabled: inputContent.length === 0}"
        :disabled="inputContent.length === 0"
      >Join</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      inputContent: ''
    }
  },
  methods: {
  },
  directives: {
    focus: {
      inserted: function (el) {
        el.focus()
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#homeSection {
  min-width: 300px;
  width: 30%;
  height: 600px;
}

</style>
