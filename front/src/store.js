import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

import Api from '@/api/Api'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
    state: {
        nodes: [],
        status: {}
    },
    actions: {
        getNodes: async ({commit}) => {
            const {data: response} = await Api().get('/nodes')
            commit('setNodes', response)
        },
        updateNode: async ({commit}, node) => {
            const {data: response} = await Api().put(`/nodes/${node.id}`, node)
            commit('updateNode', response)
        },
        deleteNode: async ({commit}, node_id) => {
            await Api().delete(`/nodes/${node_id}`)
            commit('deleteNode', node_id)
        },
        createNode: async ({commit}, node) => {
            const {data: response} = await Api().post('/nodes', node)
            commit('createNode', response)
        },
        getNodeStatus: async ({commit}, node_id) => {
            const {data: response} = await Api().get(`/nodes/${node_id}/status`)
            commit('updateNodeStatus', response)
        }
    },
    mutations: {
        setNodes: (state, nodes) => {
            state.nodes = nodes
        },
        createNode: (state, node) => {
            state.nodes.push(node)
        },
        deleteNode: (state, node_id) => {
            state.nodes = state.nodes.filter(node => node.id !== node_id)
        },
        updateNode: (state, node) => {
            state.nodes = state.nodes.map(old => (old.id === node.id ? node : old));
        },
        updateNodeStatus: (state, status) => {
            state.status = status;
        },
    },
    getters: {
        nodes: state => state.nodes,
        node: state => node_id => state.nodes.find(node => node.id === node_id),
        status: state => state.status
    }
})
