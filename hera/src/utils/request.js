import axios from "axios";
import {getToken} from "@/utils/token.js";
import {showMessage} from "@/utils/message.js";
import router from "@/router/index.js"


const service = axios.create({
    baseURL: "http://127.0.0.1:8000/",
    timeout: 50000
})


service.interceptors.request.use(config => {
    config.headers['Authorization'] = 'Bearer ' + getToken();
    return config
});

service.interceptors.response.use(res => {
    return res
}, err => {
    if (err.response.status === 401) {
        router.push('/auth/login');
    } else if (err.response.status === 403) {
        router.push('/errors/403')
    } else if (err.response.status === 500) {
        router.push('/errors/500')
    } else {
        showMessage('error', err.response.data.detail)
        return Promise.reject(err)
    }
});

export default service;
