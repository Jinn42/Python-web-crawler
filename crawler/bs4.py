
import requests
from bs4 import BeautifulSoup
#对首页的页面数据进行抓取
headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url='http://www.shicimingju.com/book/shitong.html'
page_text=requests.get(url=url,headers=headers).text
#在首页中解析出章节的标题和详情页的url
#实例化BeatifulSoup对象，需要将页面源码数据加载到该对象中
soup=BeautifulSoup(page_text,'lxml')
#解析章节标题和详情页的url
li_list=soup.select('.book-mulu > ul > li ')
fp=open('./shitong.txt','w',encoding='utf-8')
for li in li_list:
    title=li.a.string
    detail_url='http://www.shicimingju.com'+li.a['href']
#对详情页发起请求，解析出章节内容
    detail_page_text=requests.get(url=detail_url,headers=headears).text
#解析出详情页中相关的章节内容
    detail_soup=BeautifulSoup(detail_page_text,'lxml')
    div_tag=detail_soup.find('div',class_='chapter_content')
#解析到了章节的内容
    content=div_tag.text
    fp.write(title+':'+content+'\n')
    print(title,'爬取成功！！！')

