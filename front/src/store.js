import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
    state: {
        nodes: [],
    },
    actions: {
        getNodes: async ({commit}) => {
            const {data: nodes} = await axios.get('http://localhost:8080/api/nodes')
            commit('setNodes', nodes)
        },
        updateNode: async ({commit}, node) => {
            const {data: response} = await axios.put(`http://localhost:8080/api/nodes/${node.id}`, node)
            commit('updateNode', response)
        },
        deleteNode: async ({commit}, node_id) => {
            console.log(`Delete ${node_id}`)
            await axios.delete(`http://localhost:8080/api/nodes/${node_id}`)
            commit('deleteNode', node_id)
        },
        createNode: async ({commit}, node) => {
            const {data} = await axios.post('http://localhost:8080/api/nodes', node)
            commit('createNode', data)
        }
    },
    mutations: {
        setNodes: (state, nodes) => {
            state.nodes = nodes
        },
        createNode: (state, node) => {
            state.nodes.unshift(node)
        },
        deleteNode: (state, node_id) => {
            state.nodes = state.nodes.filter(node => node.id !== node_id)
        },
        updateNode: (state, node) => {
            state.nodes = state.nodes.map(old => (old.id === node.id ? node : old));
        }
    },
    getters: {
        nodes: state => state.nodes,
        node: state => node_id => state.nodes.find(node => node.id === node_id)
    }
})
