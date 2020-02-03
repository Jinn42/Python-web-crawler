import requests
import json
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#获取批量企业不同的ID值
id_list=[]
All_data_list=[]
url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
#参数的封装
for page in range(1,6):
    page=str(page)
    data={
        'on':' true',
        'page':page,
        'pageSize':' 15',
        'productName':'',
        'conditionType':' 1',
        'applyname':'',
        'applysn':''
        }
    json_id=requests.post(url=url,data=data,headers=headers).json()
    for dic in json_id['list']:
        id_list.append(dic['ID'])

#获取企业详细数据
post_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    Data={
        'id':id
     }
    detail_json=requests.post(url=post_url,data=Data,headers=headers).json()
    All_data_list.append(detail_json)

#持久化储存

fp = open('./alldata.json','w',encoding='utf-8')
json.dump(All_data_list,fp=fp,ensure_ascii=False)
print('over!!')