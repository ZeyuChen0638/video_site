import { createRouter, createWebHistory } from 'vue-router';
// 1. 定义路由组件.
import { BasicLayout } from "@/layouts"

// const RouteView = {
//   name: 'RouteView',
//   render: h => h('router-view')
// }

// 2. 定义一些路由
// 每个路由都需要映射到一个组件。
// 我们后面再讨论嵌套路由。
const routes = [
  {
    path: '/',
    component: BasicLayout,
    redirect: '/dashboard',
    children: [
      // dashboard
      {
        path: '/dashboard',
        name: 'dashboard',
        redirect: '/dashboard/hostinfo',
        meta: { key: '/dashboard', icon: () => null, label: '控制面板', title: 'Title 2' },
        children: [
          {
            path: '/dashboard/hostinfo',
            name: 'info',
            component: () => import('@/views/dashboard/HostInfo'),
            meta: { key: '/dashboard/hostinfo', icon: () => null, label: '本机信息', title: 'Title 2-1' }
          },
        ]
      },
      // video
      {
        path: '/videos',
        name: 'videos',
        meta: { key: '/videos', icon: () => null, label: '视频', title: 'Title 3'},
        redirect: '/videos/gallery',
        children: [
          {
            path: '/videos/gallery',
            name: 'video-gallery',
            component: () => import('@/views/video/Gallery'),
            meta: { key: '/videos/gallery', icon: () => null, label: '视频总览', title: 'Title 3-1' }
          }
        ]
      }
    ]
  },
]

// 3. 创建路由实例并传递 `routes` 配置
// 你可以在这里输入更多的配置，但我们在这里
// 暂时保持简单
const router = createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: createWebHistory(),
  routes, // `routes: routes` 的缩写
})

export { routes }
export default router
