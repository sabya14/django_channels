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
        },
        data: function () {
            return {
                notificationSocket: null
            }

        },
        beforeMount: function () {
            this.notificationSocket = new WebSocket(
                'ws://' + 'localhost:8000' + '/file_app/file/' + 'file_list' + '/');
            this.notificationSocket.onmessage = function (e) {
                var data = JSON.parse(e.data);
                var message = data['message'];
                window.alert("Notification " + message)
            };
            this.notificationSocket.onclose = function (e) {
                console.error('Chat socket closed unexpectedly');
            };
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
