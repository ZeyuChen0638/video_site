<template>
  <div class="main">
    <a-row :gutter="[16, 16]" justify="space-around">
      <a-col :span="6">
        <info-card>
          <template #title>
            <svg-icon iconname="icon-cpu-full" :style="{ 'font-size': '42px', 'float':'left', 'fill': 'rgba(24, 114, 157, 0.88)'}"></svg-icon>
            <span :style="{'align-self': 'center', 'margin':'10px'}">处理器</span>
          </template>
          <template #body>
            <a-row>
              <a-col :span="12">
                <a-form labelAlign="left" :label-col="{ span: 4 }" :wrapper-col="{ span: 20 }">
                  <a-form-item>
                    <template #label>
                      <b>处理器</b>
                    </template>
                    <div>{{ cpuInfo.model_name }}</div>
                  </a-form-item>
                  <a-form-item>
                    <template #label>
                      <b>频率</b>
                    </template>
                    <div>{{ cpuInfo.MHz }}</div>
                  </a-form-item>
                  <a-form-item>
                    <template #label>
                      <b>缓存</b>
                    </template>
                    <div>{{ cpuInfo.cache_size }}</div>
                  </a-form-item>
                  <a-form-item>
                    <template #label>
                      <b>核心数</b>
                    </template>
                    <div>{{ cpuInfo.cores }}</div>
                  </a-form-item>
                </a-form>
              </a-col>
              <a-col>
                <a-divider type="vertical" :style="{'height': '100%', 'margin-right':'12px'}"/>
              </a-col>
              <a-col>
                XXXX
              </a-col>
            </a-row>
          </template>
        </info-card>
      </a-col>
      <a-col :span="6">
        <info-card>
          <template #title>
            <svg-icon iconname="icon-neicun" :style="{ 'font-size': '42px', 'float':'left', 'fill': 'rgba(24, 114, 157, 0.88)'}"></svg-icon>
            <span :style="{'align-self': 'center', 'margin':'10px'}">内存</span>
          </template>
          <template #body>
            <a-row>
              <a-col :span="12">
                <a-form labelAlign="left" :label-col="{ span: 7 }" :wrapper-col="{ span: 17 }">
                  <a-form-item>
                    <template #label>
                      <b>内存总大小</b>
                    </template>
                    <div>{{ memoryInfo.total_memory }}</div>
                  </a-form-item>
                  <a-form-item>
                    <template #label>
                      <b>总交换空间</b>
                    </template>
                    <div>{{ memoryInfo.total_swap }}</div>
                  </a-form-item>
                </a-form>
              </a-col>
              <a-col>
                <a-divider type="vertical" :style="{'height': '100%', 'margin-right':'12px'}"/>
              </a-col>
              <a-col>
                XXXX
              </a-col>
            </a-row>
          </template>
        </info-card>
      </a-col>
      <a-col :span="6">
        <info-card>
          <template #title>
            <svg-icon iconname="icon-yingpan" :style="{ 'font-size': '42px', 'float':'left', 'fill': 'rgba(24, 114, 157, 0.88)'}"></svg-icon>
            <span :style="{'align-self': 'center', 'margin':'10px'}">硬盘</span>
          </template>
          <template #body>
            <a-row>
              <a-col :span="12">
                <a-form labelAlign="left" :label-col="{ span: 4 }" :wrapper-col="{ span: 20 }">
                  <a-form-item v-for="(usage, folder) in diskinfo" :key="folder">
                    <template #label>
                      <b>{{ folder }}</b>
                    </template>
                    <div>{{ usage }}</div>
                  </a-form-item>
                </a-form>
              </a-col>
              <a-col>
                <a-divider type="vertical" :style="{'height': '100%', 'margin-right':'12px'}"/>
              </a-col>
              <a-col>
                XXXX
              </a-col>
            </a-row>
          </template>
        </info-card>
      </a-col>
      <a-col :span="6">
        <info-card>
          <template #title>
            <svg-icon iconname="icon-xianka" :style="{ 'font-size': '42px', 'float':'left', 'fill': 'rgba(24, 114, 157, 0.88)'}"></svg-icon>
            <span :style="{'align-self': 'center', 'margin':'10px'}">显卡</span>
          </template>
          <template #body>
            <a-empty :image="simpleImage" />
          </template>
        </info-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { getHostInfo } from '@/api/hostinfo'
import infoCard from './components/InfoCard.vue'
import { Empty } from 'ant-design-vue';
const simpleImage = Empty.PRESENTED_IMAGE_SIMPLE;

export default {
  name: 'HostInfo',
  components:{
    infoCard
  },
  data(){
    return({
      cpuInfo: {},
      memoryInfo: {},
      diskinfo: {},
      simpleImage
    })
  },
  created(){
    getHostInfo().then(res=>{
      console.log(res)
      this.cpuInfo = res['cpu']
      this.memoryInfo = res['memory']
      this.diskinfo = res['disk']
      for (let i in this.diskinfo){console.log(i)}
    })
  }
}
</script>

<style scoped>
.cpuInfo, .memoryInfo {
  width: 48%
}
.main >>> .ant-card-head-title {
  display: flex;
}
</style>