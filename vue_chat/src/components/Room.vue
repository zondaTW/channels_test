<template>
  <div id="chatSection" class="Room container">
    <div class="row h-15">
      <div class="col" >
        <h1>Room <span class="badge badge-primary">{{roomName}}</span></h1>
      </div>
    </div>
    <div id="chatLog" class="row h-75">
      <textarea id="chat-log"></textarea>
    </div>
    <div class="row h-10">
      <input type="text" v-model="inputContent" class="w-75"/>
      <button type="button" class="btn btn-primary w-25" @click="sendMessage()">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Room',
  data () {
    return {
      roomName: '123',
      hostAdr: '127.0.0.1:8081',
      chatSocket: null,
      inputContent: ''
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
  },
  methods: {
    sendMessage: function () {
      this.chatSocket.send(JSON.stringify({
        'message': this.inputContent
      }))
      console.log('send: ' + this.inputContent)
      this.inputContent = ''
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#chatSection {
  height: 600px;
}

textarea {
  width: 150%;
}
</style>
