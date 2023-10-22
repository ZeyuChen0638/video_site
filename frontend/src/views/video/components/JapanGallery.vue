<template>
  <!-- <div>
    日本
  </div> -->
  <a-carousel autoplay>
    <div v-for="img, name in recommandImgs" :key="name">
      <img :src="img" />
    </div>
    <!-- <div><img :src="" /></div>
    <div><h3>2</h3></div>
    <div><h3>3</h3></div>
    <div><h3>4</h3></div> -->
  </a-carousel>
</template>

<script>
import { getRecommandVideo } from '@/api/japanVideo'
export default{
  name: 'japanGallery',
  mounted(){
    getRecommandVideo().then(res=>{
      console.log(res)
      this.recommandImgs = res
    })
  },
  data(){
    return({
      recommandImgs:{}
    })
  }
}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 160px;
  line-height: 160px;
  background: #364d79;
  overflow: hidden;
}

.ant-carousel >>> .slick-slide h3 {
  color: #fff;
}
</style>