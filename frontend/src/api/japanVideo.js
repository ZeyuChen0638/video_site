import request from '@/utils/request'

const videoApi = {
    RecommandInfo: '/video/recommand/',
    actorAvatar: '/video/avatar/'
}

export function getRecommandVideo () {
  return request({
    url: videoApi.RecommandInfo,
    method: 'get',
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  })
}

export function getActorAvatar () {
  return request({
    url: videoApi.actorAvatar,
    method: 'get',
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  })
}
