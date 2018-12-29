<template>
    <div class="hello">
        <h1>Upload Files</h1>
        <div>
            <input id="upload" type="file"/>
            <button @click="uploadFile">Submit</button>
        </div>
        <h1>{{ msg }}</h1>
        <div>
            <ul v-for="file in files">
                <li>{{file.name}}</li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Files',
        props: {
            msg: String
        },
        data: function () {
            return {
                files: []
            }
        },
        mounted: function () {
            this.getFilesList()
        },
        methods: {
            uploadFile: function () {
                let file = document.getElementById("upload").files[0]
                let formData = new FormData()
                formData.append("name", file.name);
                formData.append("file", file);
                this.ajaxPromise({
                    'url': "ws://localhost:8000/files/",
                    'type': "POST",
                    'data': formData,
                    'contentType': false
                }).then(data => {
                    this.getFilesList()
                }).catch(error => {
                    console.log("Error", error)
                })
            },
            getFilesList: function () {
                this.ajaxPromise({
                    'url': "ws://localhost:8000/files/",
                    'type': "GET"
                }).then(data => {
                    console.log("Response", data)
                    this.files = data
                }).catch(error => {
                    console.log("Error", error)
                })
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
