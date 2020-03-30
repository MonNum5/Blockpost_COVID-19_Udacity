
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

city_pd=pd.DataFrame([])

driver=webdriver.Firefox()
cit_list=['Gangseo-gu', 'Jungnang-gu', 'Jongno-gu', 'Mapo-gu', 'Seongbuk-gu',
       'etc', 'Songpa-gu', 'Seodaemun-gu', 'Seongdong-gu', 'Seocho-gu',
       'Guro-gu', 'Gangdong-gu', 'Eunpyeong-gu', 'Geumcheon-gu',
       'Gwanak-gu', 'Nowon-gu', 'Dongjak-gu', 'Gangnam-gu',
       'Yangcheon-gu', 'Gwangjin-gu', 'Dongdaemun-gu', 'Yeongdeungpo-gu',
       'Dobong-gu', 'Yongsan-gu', 'Gangbuk-gu', 'Jung-gu', 'Dongnae-gu',
       'Haeundae-gu', 'Yeonje-gu', 'Buk-gu', 'Nam-gu', 'Seo-gu',
       'Geumjeong-gu', 'Saha-gu', 'Suyeong-gu', 'Sasang-gu',
       'Busanjin-gu', 'Dalseo-gu', 'Dalseong-gun', 'Suseong-gu',
       'Dong-gu', 'Wuhan', 'Bupyeong-gu', 'Michuhol-gu', 'Yeonsu-gu',
       'Gyeyang-gu', 'Namdong-gu', 'Yuseong-gu', 'Daedeok-gu', 'Ulju-gun',
       'Sejong', 'Goyang-si', 'Pyeongtaek-si', 'Bucheon-si', 'Suwon-si',
       'Guri-si', 'Siheung-si', 'Gimpo-si', 'Icheon-si', 'Pocheon-si',
       'Anyang-si', 'Yongin-si', 'Paju-si', 'Namyangju-si', 'Seongnam-si',
       'Gwangmyeong-si', 'Gwacheon-si', 'Hwaseong-si', 'Osan-si',
       'Gunpo-si', 'Uiwang-si', 'Ansan-si', 'Gwangju-si', 'Anseong-si',
       'pocheon-si', 'Uijeongbu-si', 'Hanam-si', 'Gangneung-si',
       'Samcheok-si', 'Sokcho-si', 'Wonju-si', 'Chunchun-si',
       'Taebaek-si', 'Jeungpyeong-gun', 'Cheongju-si', 'Eumseong-gun',
       'Chungju-si', 'Goesan-gun', 'Danyang-gun', 'Gyeryong-si',
       'Cheonan-si', 'Asan-si', 'Seosan-si', 'Hongseong-gun', 'Gunsan-si',
       'Gimje-si', 'Jeonju-si', 'Suncheon-si', 'Yeosu-si', 'Gwangyang-si',
       'Gyeongsan-si', 'Gyeongju-si', 'Goryeong-gun', 'Gumi-si',
       'Gunwi-gun', 'Gimcheon-si', 'Mungyeong-si', 'Bonghwa-gun',
       'Sangju-si', 'Seongju-gun', 'Andong-si', 'Yeongdeok-gun',
       'Yeongyang-gun', 'Yeongju-si', 'Yeongcheon-si', 'Yecheon-gun',
       'Uiseong-gun', 'Cheongdo-gun', 'Cheongsong-gun', 'Chilgok-gun',
       'Pohang-si', 'Hapcheon-gun', 'Jinju-si', 'Changwon-si',
       'Yangsan-si', 'Geoje-si', 'Hamyang-gun', 'Goseong-gun',
       'Gimhae-si', 'Namhae-gun', 'Geochang-gun', 'Changnyeong-gun',
       'Miryang-si', 'Jeju-do']
for city in tqdm(cit_list):
    i=city_pd.shape[0]
    city_pd.at[i,'city']=city
    try:
        #Go to Citypopulation search
        driver.get("https://www.citypopulation.de/search.html")
        time.sleep(1)
        #Search for the city
        search_country= driver.find_element_by_id("countries1")
        search_country.send_keys('South Korea')
        search_place= driver.find_element_by_id("places1")
        search_place.send_keys(city)
        search_place.send_keys(Keys.RETURN)
        time.sleep(1)

        #Get first result
        result=driver.find_element_by_class_name("result")
        result.click()

        #Scrap the html
        URL=driver.current_url

        response=requests.get(URL)
        soup=BeautifulSoup(response.text,'html.parser')

        #Get the table with pupultion information
        table=soup.find('table',{"id":"ts"}).tbody
        rows = table.find_all("td")
        
        #Scrap population density and populatin number from table
        city_pd.at[i,'PopulationDensity']=re.search(r'data-density="(.*?)"', str(rows[0])).group(1)
        city_pd.at[i,'Population']=re.search(r'">(.*?)</td>', str(rows[-2])).group(1)
        time.sleep(2)
    except:
        print(f"Did not work for {city}")
        pass

driver.close()
driver.quit()
print(city_pd)

