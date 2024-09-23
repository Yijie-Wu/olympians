import axios from '@/utils/request.js'


export function get_admin_message() {
    return axios(
        {
            method: 'get',
            url: '/message/admin',
        }
    )
}
