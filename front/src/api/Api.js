import axios from 'axios'

export default () => {
    return axios.create({
        baseURL: `http://localhost/api`,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
}