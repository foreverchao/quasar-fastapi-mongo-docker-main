import request from 'src/utils/requests'

export function apiUserSignup(data) {
    return request({
        url: `/signup`,
        method: 'POST',
        data
    })
}

export function apiAllUserGet() {
    return request({
        url: '/users',
        method: 'GET',
    })
}

export function apiUserPut(id,data) {
    return request({
        url: `/users/${id}`,
        method: 'PUT',
        data
    })
}

export function apiUserDelete(id,data) {
    return request({
        url: `/users/${id}`,
        method: 'DELETE',
        data
    })
}