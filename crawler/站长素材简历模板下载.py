import requests
from lxml import etree
import os

if not os.path.exists('./cvlibs'):
    os.mkdir('./cvlibs')

headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

url='http://sc.chinaz.com/jianli/free.html'
response=requests.get(url=url,headers=headers)
response.encoding='utf-8'
page_text=response.text
tree=etree.HTML(page_text)
cv_list=tree.xpath('//div[@id="main"]/div/div/a')

for cv in cv_list:
    cv_src = cv.xpath('./img/@src')[0]
    cv_data = requests.get(url=cv_src, headers=headers).content
    cv_name = cv.xpath('./img/@alt')[0] + '.jpg'
    #cv_name = cv_name.encode('iso-8859-1').decode('gbk')
    cv_path = 'cvlibs/' + cv_name
    with open(cv_path,'wb') as fp:
        fp.write(cv_data)
        print(cv_name,'下载成功！！')
