import requests
import json
#1.指定URL
post_url='https://fanyi.baidu.com/sug'
#2.进行UA伪装
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#3.post请求参数处理（同get请求一致）
word= input('enter a word:')
data = {
    'kw':word
}
#4.请求发送
response= requests.post(url=post_url,data=data,headers=headers)
#5.获取响应数据：json()方法返回的事obj（如果确认响应数据是json类型的，才可以使用json()）
dic_obj=response.json()
#6.持久化存储
fileName = word + '.json'
fp = open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)

print('over!!')