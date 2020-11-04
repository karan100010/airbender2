import asyncio
import requests
import aiohttp
import datetime
x="<GATEWAY_ID V='861480034774069'><DT V='2020-10-03 12:15:00'><AT T='30.1' R='61.3'/><PM A='72' B='103' C='104' D='47' E='68' F='76'/><DL B='7.303' P='0.0' S='374'/></DT></GATEWAY_ID>"
async def fetch(session, url):
    start_time = datetime.datetime.now()
    print(start_time)
    async with session.post(url,data=x) as response:
        return await response.text()

async def main():
    base_url = "https://agile-depths-18594.herokuapp.com/post"
    
    urls=[base_url for i in range(10)]
    
    tasks = []
    async with aiohttp.ClientSession(trust_env=True) as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        # for html in htmls:
        #     print(html[:100])
        return tasks
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())