import re
import requests
from bs4 import BeautifulSoup
def scrapper():
    url="https://www.astrospeak.com/horoscope"
    src_code=requests.get(url)
   
    soup = BeautifulSoup(src_code.text,'html.parser')
    dict1 = {}
    links = []
    zodiacs = []
    for link in soup.findAll('a',class_="white-box"):
        href = link.get('href')
        title = link.get('title')
        dict1[title] = href
        links.append(href)
        zodiacs.append(title.upper())
    dict_horos={}
      
    for zodiac in dict1:
        src_code1=requests.get(dict1[zodiac])     
        soup1=BeautifulSoup(src_code1.text,'html.parser')
        text = soup1.find(class_="lineHght18").get_text()
        dict_horos[zodiac] = text

    return dict_horos
        
    

