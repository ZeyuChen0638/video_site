<template>
  <a-row justify="space-around" align="middle">
    <a-col :span="1">
      <div :style="{textAlign: 'center'}">
        <LeftCircleOutlined class="slick-arrow" @click="preCarousel"/>
      </div>
    </a-col>
    <a-col :span="22">
      <a-carousel autoplay :autoplaySpeed=4000 :slidesToShow=8 :style="{'width':'100%'}" ref="carousel" dots>
        <div v-for="img, name in recommandImgs" :key="name" :style="{'width':'20%'}">
          <div :style="{width:'95%', height:'17vh', overflow:'hidden', position:'relative', left:'50%', transform:'translate(-50%, 0)'}">
            <a-image :src="img" 
            :style="{
              maxWidth: '100%',
              height: '100%',
              position: 'relative',
              left: '50%',
              transform: 'translate(-50%, 0)',
              paddingTop:'2%',
              objectFit: 'contain'
            }"/> 
            <!-- <a-img :src="img" />  -->
            <span>{{name}}</span>
          </div>
        </div>
      </a-carousel>
    </a-col>
    <a-col :span="1">
      <div :style="{textAlign: 'center'}">
        <RightCircleOutlined class="slick-arrow" @click="nextCarousel"/>
      </div>
    </a-col>
  </a-row>
  <a-card>
    <div>
      <span style="margin-right: 8px">演员:</span>
      <a-space :size="[0, 8]" wrap>
        <a-checkable-tag
          v-for="tag in tags.actor"
          :key="tag"
          :checked="checkedTags.actor.indexOf(tag) != -1"
          @change="(checked) => changeSearchTag(tag, checked, 'actor')"
        >
          {{ tag }}
        </a-checkable-tag>
      </a-space>
    </div>
    <div>
      <span style="margin-right: 8px">系列:</span>
      <a-space :size="[0, 8]" wrap>
        <a-checkable-tag
          v-for="tag in tags.series"
          :key="tag"
          :checked="checkedTags.series.indexOf(tag) != -1"
          @change="(checked) => changeSearchTag(tag, checked, 'series')"
        >
          {{ tag }}
        </a-checkable-tag>
      </a-space>
    </div>
  </a-card>
  <a-card :style="{ marginTop: '24px' }" class="galleryCard">
    <a-row :gutter="[16, 16]">
      <a-col v-for="img, name in recommandImgs" :key="name" :span="3">
        <video-card
          actor='松下紗栄子'
          :cover="img"
          :videoName="name"
        />
      </a-col>
    </a-row>
  </a-card>
</template>

<script>
const Tags = {
        'actor': ['松下紗栄子', '水户香奈', '篠田步美', '泽村伶子'],
        'series': ['お色気P●A会長＆悩殺女教師と悪ガキ生徒会', '胁迫套间']
      }
import {
  LeftCircleOutlined,
  RightCircleOutlined
} from '@ant-design/icons-vue';
import { getRecommandVideo } from '@/api/japanVideo'
import videoCard from './VideoCard.vue'
export default{
  name: 'japanGallery',
  components:{
    LeftCircleOutlined,
    RightCircleOutlined,
    videoCard
  },
  mounted(){
    getRecommandVideo().then(res=>{
      console.log(res)
      this.recommandImgs = res
    })
  },
  data(){
    return({
      recommandImgs:{},
      tags: Tags,
      checkedTags: {
        actor: ['松下紗栄子', '篠田步美'],
        series: ['お色気P●A会長＆悩殺女教師と悪ガキ生徒会']
      }
    })
  },
  methods:{
    preCarousel(){
      this.$refs.carousel.prev()
    },
    nextCarousel(){
      this.$refs.carousel.next()
    },
    changeSearchTag(tag, checked, type) {
      console.log(tag, checked, type, this.checkedTags[type].indexOf(tag))
      let idx = this.checkedTags[type].indexOf(tag)
      if (idx == -1) {
        this.checkedTags[type].push(tag)
      } else {
        this.checkedTags[type].splice(idx, 1)
      }
    }
  }
}
</script>

<style scoped>
/* For demo */
.ant-carousel >>> .slick-slide {
  text-align: center;
  /* height: 40vh; */
  /* line-height: 160px; */
  background: #ffffff;
  overflow: hidden;
}

.ant-carousel >>> .slick-list {
  transform: translate(-50%, 0);
  left: 50%;
  width: 100%;
}

.ant-carousel >>> .slick-slide h3 {
  color: #ffffff;
}

.slick-arrow {
  width: 25px;
  height: 25px;
  font-size: 50px;
  color: #939393;
  /* background-color: rgba(31, 45, 61, 0.11); */
  transition: ease all 0.3s;
  opacity: 0.3;
  z-index: 1;
  cursor: pointer;
}

.slick-arrow:before{
  display: none;
}

.slick-arrow:hover {
  color: #2a2a2a;
  opacity: 0.5;
}

.ant-carousel >>> .slick-dots {
  bottom:10%;
  /* background-color: red; */
}

.galleryCard.ant-card-bordered{
  border: 0px solid #c9c9c9;;
}

</style>