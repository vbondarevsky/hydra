import axios from 'axios'

export default () => {
    return axios.create({
        // TODO: в прод версии хост указывать не нужно
        baseURL: `http://localhost:8080/api`,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
}
