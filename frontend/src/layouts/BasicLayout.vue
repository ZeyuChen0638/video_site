<template>
  <!-- <a-config-provider
    :theme="{
      algorithm: theme.darkAlgorithm,
    }"
  > -->
  <a-layout has-sider>
    <a-layout-sider
      :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0, top: 0, bottom: 0 }"
    >
      <div class="logo" />
      <a-menu
        id="router-menu"
        :inlineCollapsed=false
        v-model:openKeys="menu.openKeys"
        v-model:selectedKeys="menu.selectedKeys"
        mode="inline"
        :items="menu.items"
        theme="dark"
        @click="handleClick"
        @openChange="handleChange"
      ></a-menu>
    </a-layout-sider>
    <a-layout :style="{ marginLeft: '200px' }">
      <a-layout-header :style="{ background: '#fff', padding: 0 }" />
      <a-layout-content :style="{ margin: '24px 16px 0', overflow: 'initial' }">
        <div :style="{ padding: '24px', background: '#fff'}">
          <router-view />
        </div>
      </a-layout-content>
      <a-layout-footer :style="{ textAlign: 'center' }">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
    </a-layout>
  <!-- </a-config-provider> -->
</template>

<script>
import { theme } from 'ant-design-vue'
import { routes } from '@/router'

// import {
//   UserOutlined,
//   VideoCameraOutlined,
//   UploadOutlined,
//   BarChartOutlined,
//   CloudOutlined,
//   AppstoreOutlined,
//   TeamOutlined,
//   ShopOutlined,
// } from '@ant-design/icons-vue'

export default {
  name: 'BasicLayout',
  components: {

      // UserOutlined,
      // VideoCameraOutlined,
      // UploadOutlined,
      // BarChartOutlined,
      // CloudOutlined,
      // AppstoreOutlined,
      // TeamOutlined,
      // ShopOutlined,
  },
  data(){
    return({
      theme,
      menu: {
        items: [],
        selectedKeys: [],
        openKeys: []
      }
    })
  },
  created(){
    // console.log(this.$route)
    let indexRoute = routes.find(item=>item.path==='/')
    this.menu.items = this.createMenuItems(indexRoute.children)
  },
  watch: {
    $route:{
      immediate: true,
      handler(route) {
        let curOpenKeys = []
        for (let parentPath of route.matched) {
          curOpenKeys.push(parentPath.path)
        }
        this.menu.openKeys = [...curOpenKeys]
        this.menu.selectedKeys = [route.fullPath]
      }
    }
  },
  onUpdated(){
  },
  methods: {
    createMenuItems(routes) {
      let staticRoutes = []
      for (let route of routes) {
        if (!('children' in route)) {
          staticRoutes.push({
            key:route.meta.key,
            icon:route.meta.icon,
            label:route.meta.label,
          })
        } else {
          staticRoutes.push({
            key:route.meta.key,
            icon:route.meta.icon,
            children:this.createMenuItems(route.children),
            label:route.meta.label,
          })
        }
      }
      return staticRoutes
    },
    handleClick(menu){
      this.$router.push(menu.key)
    },
    handleChange() {

    }
  }
}
</script>

<style scoped>
.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}
</style>