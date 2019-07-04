from bs4 import BeautifulSoup
import requests
from requests import get
import pandas as pd
import itertools
import seaborn as sns
import urllib.request
import json
hotelname=[]
hotelurl=[]
address=[]
ratings=[]
hotelinfo=[]
check_in=[]
check_out=[]
rooms=[]
count=1
npage=0
for page in range(0,37):
    npage+=1
    url = "http://me.cleartrip.com/hotels/united-states/miami/?page="+str(count)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    x=soup.find_all('h2',class_='hotels-name')
    for y in x:
       count=count+1
       linkshotel=y.find('a')
       url2=linkshotel.get('href')
       print(url2)
       z='https://me.cleartrip.com'+url2
       page1 = urllib.request.urlopen(z)
       soup1 = BeautifulSoup(page1, 'html.parser')
    
       title=soup1.find('title')
       titlename=title.string
       hotelname.append(titlename)
    
       hotelurl.append(z)
    
       add= soup1.find('div', class_='amenitiesCategory')
       add1=add.find_all('p')[1].text
       address.append(add1)
    
       rating=soup1.find(class_="inline row trustBadges")
       rate=rating.find('small').text
       ratings.append(rate)
    

       abouthotel=soup1.find('div', class_='amenitiesCategory')
       about=abouthotel.find_all('p')
       for p in about:
           hotelinfo.append(p.text)
       
       chk=soup1.find('div', class_="hInfo row")
       li=chk.find_all('li')
       checkin=li[0].text
       checkout=li[1].text
       #room=li[2].text
     
       check_in.append(checkin)
       check_out.append(checkout)
       """
       if(room==" "):
       rooms.append("non avail")
       else:
       rooms.append(room)"""
       b={'hotelname':hotelname,
       'hotel-url':hotelurl,
       'address':address,
       'ratings':ratings,
       'hotel-info':hotelinfo,
       'checkin':check_in,
       'checkout':check_out
        }
          
       filename="file"+str(count)
       with open(filename, "w") as writeJSON:
          json.dump(b, writeJSON, ensure_ascii=False)




cols=['hotl-name','hotel-url','address','ratings','hotel-info','checkin','checkout']
 
a={'hotelname':hotelname,
    'hotel-url':hotelurl,
    'address':address,
    'ratings':ratings,
    'hotel-info':hotelinfo,
    'checkin':check_in,
    'checkout':check_out
    }

'''df = pd.DataFrame.from_dict(a, orient='index')
df.transpose()

df.to_excel('miamihotel2.xls')'''

with open("textbooks.json", "w") as writeJSON:
   json.dump(a, writeJSON, ensure_ascii=False)


