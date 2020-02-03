import requests
from lxml import etree
#爬取58二手房的租房信息
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#爬取到页面数据源码
url='https://gm.58.com/glparis-sl/glslfangwuchuzu/?PGTID=0d000000-05d3-d4a1-231f-80e49e3933f7&ClickID=1'
page_text=requests.get(url=url,headers=headers).text

#数据解析
tree=etree.HTML(page_text)
#存储的就是a标签对象
a_list=tree.xpath('//div[@class="info-content"]/a')
fp = open('58.txt','w',encoding='utf-8')
for a in a_list:
    title = a.xpath('./div/p/text()')[0]
    print(title)
    fp.write(title+'\n')

