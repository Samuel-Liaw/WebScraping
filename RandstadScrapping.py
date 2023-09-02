from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.randstad.co.jp/tenshoku/result/?path=P0001&n3l=7000000&q=データアナリスト&s8=1&s8=4&s9=10&s9=11&s9=12&s9=13&s10=15&s10=18'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

joblist = []

jobs = soup.find_all('div', class_="rs-job rs-job--bordered-top rs-job--shadow")
# print(jobs)

for job in jobs:
    title = job.find('a', class_="rs-job__title").text
    try:
        des = job.find('div', class_="rs-job-features__item").text
    except AttributeError:
        des = 'None'
    category = job.find_all('dd', class_="rs-condition-list__text")[1].text
    salary_min = int(job.find('span', class_="rs-text-salary").string.split('〜')[0].replace(',',''))
    salary_max = int(job.find('span', class_="rs-text-salary").string.split('〜')[1].replace(',',''))
    list = {'Job_Title': title,
            'Job_Description': des,
            'Job_Category': category,
            'Salary_Min': salary_min,
            'Salary_Max': salary_max}
    joblist.append(list)
df = pd.DataFrame(joblist)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
df.to_excel('job.xlsx')
print(df)