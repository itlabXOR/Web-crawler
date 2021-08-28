import requests
from bs4 import BeautifulSoup
import csv
def newscrawler():
    #구글 뉴스url
    url="https://news.google.com"
    #나스닥 링크 필요시에 이것만 변경해서 원하는 종목 크롤링 가능
    news_url=url+"/search?q=Nasdaq&hl=en-US&gl=US&ceid=US%3Aen"

    stocknews=requests.get(news_url)
    html_src=stocknews.text
    soup=BeautifulSoup(html_src,'html.parser')

    #div xrnccd 속성 부분 추출
    news=soup.select('div[class="xrnccd"]')
    #현재 크롤링한 뉴스 개수
    print(len(news))
    #xrnccd 태그의 내용들
    #print(news[0])
    #print("\n")
    #제목이 있는 h3태그의 ipQwMb ekueJc RD0gLb
    test = news[0].select('h3[class="ipQwMb ekueJc RD0gLb"]')
    print(test)
    for article in news:
        #제목 a태그에 DY5T1d속성
        news_title = article.find('a', attrs={'class': 'DY5T1d'}).getText()

        news_report = article.find('time', attrs={'class': 'WW6dff uQIVzc Sksgp'})
        news_datetime = news_report.get('datetime').split('T')

        news_date = news_datetime[0][:-1]
        news_time = news_datetime[1][:-1]

        result = news_date, news_time, news_title
        print(result)



print(newscrawler())



