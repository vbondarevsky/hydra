<template>
    <div class="about">
        <label for="name">Name</label><input type="text" id="name" v-model="name">
        <label for="url">URL</label><input type="text" id="url" v-model="url">
        <button @click="addNode">Добавить</button>
        <p>Name: {{ name }}, ULR: {{ url }}</p>

        <table border="1">
            <thead>

            <tr>
                <th>id</th>
                <th>name</th>
                <th>url</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="node in nodes">
                <td>{{node.id}}</td>
                <td>{{node.name}}</td>
                <td>{{node.url}}</td>
                <td><span @click="">edit</span></td>
                <td><span @click="deleteNode(node.id)">del</span></td>
                <td><span @click="getNodeStatus(node.id)">status</span></td>
                <td>{{node.status}}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        data() {
            return {
                name: "",
                url: ""
            }
        },
        methods: {
            ...mapActions([
                'createNode',
                'deleteNode',
                'getNodeStatus',
            ]),
            addNode() {
                this.createNode({name: this.name, url: this.url})
            }
        },
        computed: {
            ...mapGetters([
                'nodes',
                'status',
            ])
        },
        created() {
            this.$store.dispatch('getNodes')
        }
    }
</script>
