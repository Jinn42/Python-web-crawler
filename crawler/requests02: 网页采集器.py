import requests
# UA 伪装：将对应的User-Agent封装到一个字典里
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url='https://www.sogou.com/web'
#处理url携带的参数：封装到字典中
kw=input('enter a word:')
param={
    'query':kw
}
#对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
response=requests.get(url=url,params=param,headers=headers)

page_text=response.text
fileName=kw+'.html'
with open (fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
    print(fileName,'保存成功！！！')
