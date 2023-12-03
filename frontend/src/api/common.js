import request from "@/utils/request"

const commonApi = {
    listdir: '/common/listdir/'
}

export function getDirs (params) {
  return request({
      url: commonApi.listdir,
      method: 'get',
      params,
      headers: {
      "Access-Control-Allow-Origin": "*"
      }
  })
}