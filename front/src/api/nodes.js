import Api from '@/api/Api'

export default {
    getNodes() {
        return Api().get('/nodes')
    }
}