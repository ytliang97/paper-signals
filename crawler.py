import requests
from bs4 import BeautifulSoup

def trade_spider(pageType,timeType):
    url = 'http://www.cwb.gov.tw/V7/forecast/town368/towns/6600400.htm?type=' + str(pageType) + '&time=' + str(timeType)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('span', {'class': 'Forecast-box-mor1'}):
        s = link.string
        print(s)

time = '7Day'
trade_spider(Weather,time)