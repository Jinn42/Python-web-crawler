import requests
from lxml import etree

headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

url='https://www.aqistudy.cn/historydata/'
page_text=requests.get(url=url,headers=headers).text
all_city_name=[]
tree=etree.HTML(page_text)
#热门城市：//div[@class="hot"]/div[@class="bottom"]/ul/li/a
#一般城市：//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a
city_name_list=tree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li/a | //div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a')
for a in city_name_list:
    city_name = a.xpath('./text()')[0]
    all_city_name.append(city_name)
print(all_city_name)