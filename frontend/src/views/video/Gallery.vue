<template>
    <div>
    <a-tabs default-active-key="JP">
      <a-tab-pane key="JP" tab="日本">
        <japan-gallery />
      </a-tab-pane>
      <a-tab-pane key="EN" tab="欧美">
        欧美
      </a-tab-pane>
    </a-tabs>
  </div>
</template>

<script>
import japanGallery from './components/JapanGallery.vue'

export default{
  name: 'videoGallery',
  components:{
    japanGallery
  },
  data(){
    return({

    })
  },
  methods:{
  }
}
</script>