<template>
  <a-card hoverable style="width: 250px" :bodyStyle="{'padding': '12px'}">
    <template #cover>
      <img
        :alt="videoName"
        :src="cover"
      />
    </template>
    <!-- <template #actions>
      <setting-outlined key="setting" />
      <edit-outlined key="edit" />
      <ellipsis-outlined key="ellipsis" />
    </template> -->
    <a-card-meta :title="videoName">
      <template #avatar>
        <a-avatar :src="avatar" />
      </template>
    </a-card-meta>
  </a-card>
</template>

<script>
import { getActorAvatar } from '@/api/japanVideo' 
export default{
  name: 'videoCard',
  props:{
    actor: {type: String, required: true},
    cover: {type: String},
    videoName: {type: String, required: true}
  },
  data(){
    return({
      avatar: ""
    })
  },
  created(){
    getActorAvatar().then(res => {
      this.avatar = res
    })
  },
  methods:{

  }
}
</script>

<style scoped>
.ant-card-bordered{
  border: 1px solid #c9c9c9;;
}
</style>
