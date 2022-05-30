import request from 'src/utils/requests'

export function apiUserLogin(data) {
    return request({
        url: '/login',
        method: 'POST',
        data
    })
}