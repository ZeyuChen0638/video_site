import { createStore } from 'vuex'
import routes from '@/router'

// 创建一个新的 store 实例

const store = createStore({
  state () {
    return {
      count: 0,
      routes
    }
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

export default store