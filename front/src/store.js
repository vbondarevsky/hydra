import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex);
Vue.use(VueAxios, axios);

export default new Vuex.Store({
    state: {
        nodes: []
    },
    mutations: {
        SET_NODES(state, nodes) {
            state.nodes = nodes;
        }
    },
    actions: {
        loadNodes({commit}) {
            axios
                .get('http://localhost:8080/api/nodes')
                .then(r => r.data)
                .then(nodes => {
                    commit('SET_NODES', nodes)
                })
        }
    }
})
