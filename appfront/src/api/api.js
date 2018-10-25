import axios from 'axios';

function getCookie (name) {
      var value = '; ' + document.cookie
      var parts = value.split('; ' + name + '=')
      if (parts.length === 2) return parts.pop().split(';').shift()
    }

let base = '';

//django后台请求统一前缀
let base_url = 'http://127.0.0.1:8000';
// let local_host = 'http://127.0.0.1:8000'

var instance = axios.create({
 headers: {'content-type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie("csrftoken") }
});

//读取账户余额提醒信息
export const systemMessageList = params =>{

    return instance.post(`${base_url}/readMessage`, { params: params });
}

//搜索账户余额提醒信息
export const searchMessageList = params =>{

    return instance.post(`${base_url}/searchMessage`, { params: params });
}

//标记账户余额提醒消息已读
export const signRead = params => {

    return instance.post(`${base_url}/signRead`, { params: params });
}

//批量标记已读
export const signBatch = params => {

    return instance.post(`${base_url}/signBatch`, { params: params });
}

