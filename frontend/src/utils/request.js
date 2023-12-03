import axios from 'axios'

// axios.defaults.withCredentials=true
// axios.defaults.crossDomain=true
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'

// 创建 axios 实例
const request = axios.create({
// API 请求的默认前缀
//   baseURL: process.env.VUE_APP_API_BASE_URL,
  baseURL: "http://localhost:8000/",
  timeout: 6000 // 请求超时时间
})

request.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    console.log(error)
    return Promise.reject(error)
  }
)

export default request
