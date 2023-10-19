import request from '@/utils/request'

const dashboardApi = {
  HostInfo: '/dashboard/hostinfo/',
  testpcd: '/dashboard/testpcd/'
}

export function getHostInfo () {
  return request({
    url: dashboardApi.HostInfo,
    method: 'get',
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  })
}
