import requests
#如何爬取图片数据
url='http://i0.xiaohua.fd.zol-img.com.cn/t_s600x5000/g5/M00/04/00/ChMkJld5zFGIQNp9AAErYvZ77eQAATNZwP956IAASt6580.jpg'
#content返回的是二进制的图片数据
#  text（字符串）；content（二进制）；json（对象）
image_data= requests.get(url=url).content
with open('./comparison.jpg','wb') as fp:
    fp.write(image_data)