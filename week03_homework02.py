import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client=MongoClient('localhost',27017)
db=client.dbhomework

#headers 질문 언제 넣어야 하는지?
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    rank = tr.select_one('td:nth-child(2)').text[0:2].strip()
    title = tr.select_one('td.info > a:nth-child(1)').text.strip()
    singer = tr.select_one('td.info > a:nth-child(2)').text

    print(rank, title, singer)
    doc={
        'rank': rank,
        'title': title,
        'singer':singer
    }
    db.dbhomework.insert_one(doc)




