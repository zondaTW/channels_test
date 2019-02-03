<template>
  <div class="hello">
    <h1>Room: {{roomName}}</h1>
    <textarea id="chat-log" cols="100" rows="20"></textarea><br/>
    <input id="chat-message-input" type="text" size="100" v-model="inputContent" /><br/>
    <input id="chat-message-submit" type="button" value="Send" @click="send_message()" />

  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      roomName: '123',
      hostAdr: '127.0.0.1:8081',
      chatSocket: null,
      inputContent: ''
    }
  },
  methods: {
    send_message: function () {
      this.chatSocket.send(JSON.stringify({
        'message': this.inputContent
      }))
      console.log('send: ' + this.inputContent)
      this.inputContent = ''
    }
  },
  mounted: function () {
    this.chatSocket = new WebSocket(
      'ws://' + this.hostAdr + '/ws/chat/' + this.roomName + '/')
    this.chatSocket.onmessage = function (e) {
      var data = JSON.parse(e.data)
      var message = data['message']
      document.querySelector('#chat-log').value += (message + '\n')
      console.log('message:' + message)
    }
    this.chatSocket.onclose = function (e) {
      console.error('Chat socket closed unexpectedly')
      console.log('close:')
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
