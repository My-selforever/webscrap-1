from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

cd = webdriver.Chrome(
    'C:/Users/todbh/Downloads/chromedriver_win32/chromedriver.exe')

cd.get(url)

time.sleep(10)

r = []

header = ['V_Mag', 'Name', 'Nayer_Designation', 'Distance',
          'Spectral_class', 'mass', 'radius', 'Luminosity']

def scrap():
    bs = BeautifulSoup(cd.page_source,'html.parser')
    tbl = bs.find("table")
    alltr = bs.find_all("tr")
    for eachtr in alltr:
        alltd = eachtr.find_all("td")
        t = []
        for index,eachtd in enumerate(alltd):
            if(index==1):
                t.append(eachtd.find_all("a")[0].contents[0])
            else:
                try:
                    t.append(eachtd.contents[0])
                except:
                    t.append("")
    r.append(t)


scrap()
print(r)
