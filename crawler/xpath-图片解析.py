import requests
from lxml import etree
import os
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#爬取到页面数据源码
url='http://pic.netbian.com/4kdongman/'
page_text=requests.get(url=url,headers=headers).text

#创建一个文件夹
if not os.path.exists('./piclibs'):
    os.mkdir('./piclibs')

#数据解析：scr的属性值，alt属性
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="slist"]/ul/li')
for li in li_list:
    img_src='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
    #通用处理中文乱码的解决方案
    img_name=img_name.encode('iso-8859-1').decode('gbk')
    print(img_name,img_src)

    #请求图片进行持久化存储
    img_data=requests.get(url=img_src,headers=headers).content
    img_path='piclibs/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功！！')
