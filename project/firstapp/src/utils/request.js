import axios from 'axios'
import { Message, MessageBox } from 'element-ui'
 
// 创建axios实例
const service = axios.create({
  baseURL: process.env.BASE_API, // api的base_url
  timeout: 15000 // 请求超时时间
})
 
// request请求拦截器，每次请求接口前都会执行这个
service.interceptors.request.use(config => {
  //可以在这里设置请求头等内容
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(error)
})
 
// respone相应拦截器
service.interceptors.response.use(
  response => {
  //这里是获取返回值，例如mall系统的后端返回内容是 code,data,message
  //所以我们拿到code，判断是否等于200，不是就走接口错误的处理方式
    const res = response.data
    if (res.code !== 200) { //处理错误的方式
      return Promise.reject('error')
    } else {//处理正确的方式
      return response.data
    }
  },
  error => {
    console.log('err' + error)// for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 3 * 1000
    })
    return Promise.reject(error)
  }
)
 
//输出对象
export default service

