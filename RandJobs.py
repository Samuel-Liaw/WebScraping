from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
           }

# s = HTMLSession()
joblist = []
pages = range(1,51)
for page in pages:
    url = f'https://www.randstad.co.jp/tenshoku/result/?limit=100&p={page}'

    r = requests.get(url, headers=headers)
    # print(r.status_code)
    soup = BeautifulSoup(r.content, 'lxml')
    # print(soup.prettify())

    jobs = soup.find_all('div', class_='rs-job__inner')
    for job in jobs:
        jobtitle = job.find('a',class_="rs-job__title").text
        # salary = job.find('span', class_="rs-text-salary").text
        speclist = job.find_all('dd', class_="rs-condition-list__text")
        salary = speclist[0].text
        jobdes = speclist[1].text
        loc = speclist[2].text
        link = job.find('a',class_="rs-job__title").get('href')
        dic = {
            'JobTitle':jobtitle,
            'JobDes':jobdes,
            'Salary':salary,
            'Location':loc,
            'Link':link
        }
        joblist.append(dic)

# print(joblist)
df = pd.DataFrame(joblist, columns=['JobTitle','JobDes','Salary','Location','Link'])
df.to_excel('randjob.xlsx')
