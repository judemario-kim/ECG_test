import requests
import pandas as pd
from bs4 import BeautifulSoup

#지오 코딩
from geopy.geocoders import Nominatim

def geocoding_reverse(lat_lng_str): 
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(lat_lng_str)

    return address

def crawl_weather_data(n, e):
    ne = n+", "+e
    address = geocoding_reverse(ne)
    # 끝
    tmp = str(address).replace(" ","").split(',')
    tmp.reverse()
    #city = str(address).split(',')[0]
    if len(tmp) > 4:
        city = tmp[4]
    else:
        city = tmp[3]

    urlValue = 'https://search.naver.com/search.naver?query={}날씨'.format(city)
    html = requests.get(urlValue)
    #pprint(html.text)
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('section', {'class': 'sc_new cs_weather_new _cs_weather'})
    weather = data1.find('span', {'class' : 'weather before_slash'}).text
    dust1 = data1.find('ul' , {'class' : 'today_chart_list'})
    dust2 = dust1.find_all('li', {'class' : 'item_today level2'})
    temp = data1.find('div',{'class' : 'temperature_text'}).find('strong').text.replace("현재 온도","")
    return_list = [weather, temp]
    for i in dust2:
        #stitle = i.find('strong', {'class':'title'}).text
        return_list.append(i.find('span', {'class':'txt'}).text)
    #return_list 0: weather, 1: temp, 2: micro_dust, 3: tmicro_dust, 4: uv_ray
    return return_list