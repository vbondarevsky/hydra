<template>
    <div class="about">
        <table border="1">
            <thead>
            <button>Добавить</button>
            <tr>
                <th>id</th>
                <th>name</th>
                <th>host</th>
                <th>port</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="node in nodes">
                <td>{{node.id}}</td>
                <td>{{node.name}}</td>
                <td>{{node.host}}</td>
                <td>{{node.port}}</td>
                <td><span @click="">edit</span></td>
                <td><span @click="deleteNode(node.id)">del</span></td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import {mapGetters, mapActions} from 'vuex'

    export default {
        methods: {
            ...mapActions([
                'createNode',
                'deleteNode'
            ])
        },
        computed: {
            ...mapGetters([
                'nodes'
            ])
        },
        created() {
            this.$store.dispatch('getNodes')
        }
    }
</script>
