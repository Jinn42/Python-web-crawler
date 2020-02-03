# request是基于同步的操作，因此在异步协程实现中应使用aiohttp模块

import asyncio
import time
import aiohttp

start = time.time()
urls = [
'https://www.baidu.com/', 'https://www.sogou.com', 'https://www.goubanjia'
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get(),post()
        #headers.params/data,prox='http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符串形式的相应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            #注意：获取相应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
tasks= []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('总耗时：', end - start)