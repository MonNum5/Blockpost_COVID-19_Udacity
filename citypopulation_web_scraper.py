import os
import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import numpy as np

df_dict={}
for file in os.listdir('coronavirusdataset/'):
    df=pd.read_csv('coronavirusdataset/'+file)
    df_dict[file.split('.')[0]]=df
    print(file.split('.')[0])
    print(df.head())

from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

df=df_dict['Region']


driver=webdriver.Firefox()

for i in tqdm(range(df.shape[0])):
    match=False
    city=df['city'][i]
    province=df['province'][i]
    
    try:
        #Go to Citypopulation search
        driver.get("https://www.citypopulation.de/search.html")
        time.sleep(2)
        #Search for the city

        search_country= driver.find_element_by_id("countries1")
        search_country.send_keys('South Korea')
        search_place= driver.find_element_by_id("places1")
        search_place.send_keys(city)
        search_place.send_keys(Keys.RETURN)
        time.sleep(3)

        #Get result element
        results=driver.find_elements_by_class_name("result")
        #check results, since a lot of the cities have the same name we also consider the province, since for a metropolitan citiy the province is the city itself it gets its on case
        for result in results:
            if province in result.text:
                match=True
                result.click()
                break
            elif 'Metropolitan  City'  in result.text:
                match=True
                result.click()
                break
    

        if match==True:
            time.sleep(3)
            #Scrap the html
            URL=driver.current_url

            response=requests.get(URL)
            soup=BeautifulSoup(response.text,'html.parser')

            #Get the table with pupultion information
            table=soup.find('table',{"id":"ts"}).tbody
            rows = table.find_all("td")
            
            #Scrap population density and populatin number from table
            df.at[i,'PopulationDensity']=float(re.search(r'data-density="(.*?)"', str(rows[0])).group(1))
            df.at[i,'Population']=float(re.search(r'">(.*?)</td>', str(rows[-2])).group(1).replace(',',''))
            time.sleep(1)
        else:
          print(f'No match for {city} in {province}')  
    except:
        print(f'Did not work for {city} in {province}')

driver.close()
driver.quit()

df.to_excel('Region_with_population_population_density.xlsx')
print(df)