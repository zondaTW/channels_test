<template>
  <div id="chatSection" class="Room container">
    <div class="row h-15">
      <div class="col" >
        <h1><span class="badge badge-primary">Room: {{roomName}}</span></h1>
      </div>
    </div>
    <div class="row h-75">
      <textarea id="chatLog" v-model="chatLogContent"></textarea>
    </div>
    <div class="row h-10">
      <input type="text" v-model="inputContent" class="w-75" v-on:keyup.enter="sendMessage()" v-focus/>
      <button type="button" class="btn btn-primary w-25" @click="sendMessage()">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Room',
  data () {
    return {
      roomName: 'test',
      hostAdr: '127.0.0.1:8081',
      chatSocket: null,
      inputContent: '',
      chatLogContent: ''
    }
  },
  mounted: function () {
    this.chatSocket = new WebSocket(
      'ws://' + this.hostAdr + '/ws/chat/' + this.roomName + '/')
    this.chatSocket.onmessage = this.onMessage
    this.chatSocket.onclose = this.onClose
  },
  methods: {
    sendMessage: function () {
      this.chatSocket.send(JSON.stringify({
        'message': this.inputContent
      }))
      console.log('send: ' + this.inputContent)
      this.inputContent = ''
    },
    onMessage: function (e) {
      var data = JSON.parse(e.data)
      var message = data['message']
      this.chatLogContent += ('> ' + message + '\n')
      console.log('message:' + message)
    },
    onClose: function (e) {
      console.error('Chat socket closed unexpectedly')
      console.log('close:')
    }
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

#chatSection {
  height: 600px;
}

#chatLog {
  width: 150%;
  overflow-x: hidden;
  overflow-y: scroll;
}
</style>
