<template>
  <div>
    <a-button @click="viewWorkflow">创建视频处理任务</a-button>
    <a-modal :open="show" title="Basic Modal" @ok="handleOk" @cancel="()=>{show=false}" destroyOnClose>
      
    </a-modal>
    
  </div>
</template>

<script>
import { getDirs } from '@/api/common'
export default{
  name: 'videoWorkflow',
  components:{

  },
  data(){
    return({
      show: false
    })
  },
  methods:{
    viewWorkflow(){
      this.show = true
      getDirs({path:"/media/sf_Porn/"}).then(res => {
        console.log(res)
      })
    },
    handleOk(){
      this.show = false
    }
  }
}
</script>