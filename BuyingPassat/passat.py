
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open("passat.html") as fp:
  soup = BeautifulSoup(fp, "html.parser")

table1 = soup.find_all("tr",class_="searchResultsItem")



veri2 = np.empty(shape=(1,6),dtype='<U4')

for row in table1:
    #foto = row.find("td",class_="searchResultsLargeThumbnail")
    #model = row.find("td", class_="searchResultsTagAttributeValue")
    #ilan = row.find("td", class_="searchResultsTitleValue
    
    try:
        foto = row.find("td",class_="searchResultsLargeThumbnail")

        ozellikler1 = row.find_all("td",class_="searchResultsTagAttributeValue")
        marka = re.split("\n", ozellikler1[0].text)[1].replace(' ','')
        seri = re.split("\n", ozellikler1[1].text)[1].replace(' ','')
        model = re.split("\n", ozellikler1[2].text)[1].replace(' ','')

        ilan = row.find("td",class_="searchResultsTitleValue").text
        ilan = re.split("\n", ilan)

        
        #model = re.split("\n",model)[1].replace(' ','')
        #ilan = row.find("td",class_="searchResultsTitleValue").text.encode("utf-8")
        

        ozellikler2 = row.find_all("td",class_="searchResultsAttributeValue")
        yil = int(re.split("\n",ozellikler2[0].text)[1].replace(' ',''))
        km = int(re.split("\n",ozellikler2[1].text)[1][:-4].replace(' ',''))

        
        fiyat = row.find("td", class_="searchResultsPriceValue").text
        fiyat = int(re.split("\n", fiyat)[1][:-7].replace('.',''))
        
    except:
        None

    
    e = np.array([[marka, seri, model, yil, km, fiyat]])
    c = np.vstack((veri2, e))
    veri2 = c
    
veri2 = np.delete(veri2,0,0)
df = pd.DataFrame(veri2,columns=('marka','seri', 'model','yil','km','fiyat'))
df = df.astype({'yil':int, 'km':int, 'fiyat':int})


df2 = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
                  columns=['length', 'width', 'species'])


#print(df.plot.scatter(x='yil', y='km',c='DarkBlue'))
ax1 = df2.plot.scatter(x='length',
                       y='width',
                       c='DarkBlue')
print(ax1)
#print(veri2)
