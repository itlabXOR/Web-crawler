import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy

time_data = []
title_data = []

def newscrawler():
    #구글 뉴스url
    url="https://news.google.com"
    #나스닥 링크 필요시에 이것만 변경해서 원하는 종목 크롤링 가능
    news_url=url+"/search?for=nasdaq+stocks&hl=en-US&gl=US&ceid=US%3Aen"


    stocknews=requests.get(news_url)
    html_src=stocknews.text
    soup=BeautifulSoup(html_src,'html.parser')
    #div xrnccd 속성 부분 추출
    news=soup.select('div[class="xrnccd"]')

    #현재 크롤링한 뉴스 개수

    print(len(news))
#데이터 가져와서 각 시간별 수치와 그래프 비교
    result = []
    for article in news:
        #제목 a태그에 DY5T1d속성
        news_title = article.find('a', attrs={'class': 'DY5T1d'}).getText()

        news_report = article.find('time', attrs={'class': 'WW6dff uQIVzc Sksgp'})
        news_datetime = news_report.get('datetime').split('T')

        news_date = news_datetime[0][:-1]
        news_time = news_datetime[1][:-1]

        result.append(news_date)
        result.append(news_time)
        result.append(news_title)
    return result
n=3
def split_list(l, n):
    # 리스트 l의 길이가 n이면 계속 반복
    for i in range(0, len(l), n):
        yield l[i:i + n]

result = split_list(newscrawler(),n)
result = result.transpose()



with open('newstitle.csv', 'w+',newline='') as f:
    write = csv.writer(f)
    write.writerow(result)
