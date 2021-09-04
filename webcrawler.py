import requests
from bs4 import BeautifulSoup
import pandas as pd

result = []


def newsurl():
    # 나스닥 주요 주식들 리스트
    news_keyword = ["Apple", "microsoft", "Amazon", "facebook", "tesla", "NVIDIA", "PayPal", "Intel", "Netflix",
                    "Adobe", "Alphabet+Inc", "ASML+Holding", "Comcast+Corporation", "Broadcom"]
    return news_keyword


def newscrawler():


    news_keyword = newsurl()
    print(len(news_keyword))
    # 구글 뉴스url
    url = "https://news.google.com"
    # 나스닥 링크 필요시에 이것만 변경해서 원하는 종목 크롤링 가능

    for i in range(-1,12):
        print(i)
        news_url = url + "/search?q=" + news_keyword[i] + "&hl=en-US&gl=US&ceid=US%3Aen"

        stocknews = requests.get(news_url)
        html_src = stocknews.text
        soup = BeautifulSoup(html_src, 'html.parser')
        # div xrnccd 속성 부분 추출
        news = soup.select('div[class="xrnccd"]')

        # 현재 크롤링한 뉴스 개수

        print(len(news))

        for article in news:
            # 제목 a태그에 DY5T1d속성
            news_title = article.find('a', attrs={'class': 'DY5T1d'}).getText()

            news_report = article.find('time', attrs={'class': 'WW6dff uQIVzc Sksgp'})

            news_datetime = news_report.get('datetime').split("T")


            news_date = news_datetime[0][:-1]
            news_time = news_datetime[1][:-1]
            # rseult 라는 리스트에 날짜 시간 제목 이란 데이터 넣기
            result.append(news_date)
            result.append(news_time)
            result.append(news_title)

    return result


n = 3


def split_list(l, n):
    # 리스트 l의 길이가 n이면 계속 반복
    for o in range(0, len(l), n):
        yield l[o:o + n]


# 리스트 값들 3개를 한묶음으로 날짜,시간,제목
result = split_list(newscrawler(), n)

# 크롤링한 데이터 데이터 프레임으로 만들기
df = pd.DataFrame.from_records(result, columns=['date', 'time', 'title'])

df = df.sort_values(by=['date', 'time'], ignore_index=True)
# 엑셀파일로 크롤링한 데이터 저장
df.to_excel('test.xlsx', encoding='utf-8')
