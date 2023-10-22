import request from '@/utils/request'

const videoApi = {
    RecommandInfo: '/video/recommand/'
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
