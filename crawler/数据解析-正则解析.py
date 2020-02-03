import requests
import re
import os

headers={
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
#创建一个文件夹，保存所有的图片
if not os.path.exists('./qiutulibs'):
    os.mkdir('./qiutulibs')
#设置一个通用的url模版
url='http://xiaohua.zol.com.cn/qutu/qiushi/%d.html'
for pageNum in range(1,3):
    #对应页码的url
    new_url=format(url%pageNum)

    #使用通用爬虫对一整张页面进行爬取
    page_text=requests.get(url=new_url,headers=headers).text
    #使用聚焦爬虫将页面中所有的图片进行爬取
    #每张图片的提取地址
#< divclass ="summary-text" >
#< a target="_blank" href="/detail48/47789.html" >
#< img loadsrc="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/0E/07/ChMkJ1dFQ4yIPWmMAAppPjmHjqYAAR3hALa_Y4ACmlW020.gif" alt="就这样轻易的狗带了" title="点击查看大图" >
#< / a >
#< / div >


    ex='< div class ="summary-text" >.*?<img loadsrc="(.*?)" alt.*? title="点击查看大图" >< / div >'
    img_sre_list=re.findall(ex,page_text,re.S)
    print(img_sre_list)
    for src in img_sre_list:
        #请求到了图片的二进制数据
        image_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[-1]
        #图片存储的路径
        imgpath='./qiutulibs'+img_name

        with open(imgpath,'wb') as fp:
            fp.write(image_data)
            print(img_name,'下载成功')



