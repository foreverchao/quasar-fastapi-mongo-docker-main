import axios from 'axios'
import { Notify } from 'quasar'
import { SessionStorage } from 'quasar'
import { apiBaseUrl } from "src/api/config"

const position = 'top'

// create an axios instance
const service = axios.create({
    baseURL: apiBaseUrl // api 的 base url
})

// request interceptor
service.interceptors.request.use(
    config => {
        const token = SessionStorage.getItem("token")
        config.headers['Authorization'] = `Bearer ${token}`
        return config
    },
    error => {
        // Do something with request error
        console.log(error) // for debug
        Promise.reject(error)
    }
)


// response interceptor
service.interceptors.response.use(
    function (response) {
        // Do something with response data
        if (response){
            switch (response.status) {
            case 200:
                NotifyCreate("Success: ",response);
                
                // go to 200 page
                break
            case 201:
                NotifyCreate("Success: ",response);
                // go to 201 page
                break
            default:
                NotifyCreate("Success Defalt: ",response);
                //console.log(error.response.data)
            }
        } 
        return response;
    },
    
    function (error) {
        console.log(error)
        if (error.response){
            switch (error.response.status) {
            case 400:
                NotifyCreate("ERROR: ",error);
                // go to 404 page
                break
            case 404:
                NotifyCreate("ERROR: ",error);
                // go to 404 page
                break
            case 500:
                //console.log("Internal Server Error");
                NotifyCreate("Internal Server Error",error);
                // go to 500 page
                break
            default:
                NotifyCreate("ERROR Defalt: ",error);
                //console.log(error.response.data)
            }
        } 
        if (!window.navigator.onLine) {
            Notify.create({
                color: 'red',
                position,
                type:'negative',
                message: "network problem, please try again later"
            })
            return;
        }
        return Promise.reject(error);
    }
)

function NotifyCreate(title,response){

    const isSuccess = response.status === 200 || response.status === 201
    
    var msg = ''
    if (isSuccess) {
        console.log(response)
        msg = response.request.statusText
    }
    else
        msg = response.response.data.detail

    Notify.create({
        color: isSuccess ? 'green' : 'red',
        position,
        type: isSuccess ? 'positive': 'negative',
        message: title + msg
    })

}

export default service

