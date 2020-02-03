import requests
import json
#1.指定URL
url='https://movie.douban.com/j/chart/top_list'
#2.进行UA伪装
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#3.post请求参数处理（同get请求一致）

param = {
'type': '24',
'interval_id': '100:90',
'action':'',
'start': '0',#从库中第几部电影去取
'limit':'20' #一次取的电影个数

}

response= requests.get(url=url,params=param,headers=headers)

list_data=response.json()


fp = open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)

print('over!!')