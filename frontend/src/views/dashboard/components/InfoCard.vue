<template>
  <a-card :style="{'height':'100%'}">
    <template #title>
      <slot name="title"></slot>
    </template>
    <slot name="body"></slot>
  </a-card>
</template>

<script>
export default {
  name: 'infoCard',
  data(){
    return({

    })
  }
}
</script>