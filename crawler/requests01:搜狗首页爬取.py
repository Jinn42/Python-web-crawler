#requirement：scrapy the homepage of Sogou
import requests
#step1: assign URL
url='http://www.sogou.com/'
#step2: send requests(get returns a response)
response=requests.get(url=url)
#step3: get response(text returns strings)
page_text=response.text
print(page_text)
#step4: durable storage of response
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
print('The ending of scrapy!!!')