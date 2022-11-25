from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/delft/page-"

for pages in range(1,5):
    page =requests.get(url+str(pages))
    soup=BeautifulSoup(page.content,'html.parser')
    lists= soup.find_all('section', class_="listing-search-item")
    with open('Delft_rental_price.csv','a',encoding='utf8',newline='') as files:
        thewriter=writer(files)
        for list in lists:
            title = list.find('a', class_="listing-search-item__link--title").text.replace('\n','')
            location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n','')
            price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
            area = list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
            room = list.find('li', class_="illustrated-features__item--number-of-rooms").text.replace('\n','')
            furniture = getattr(list.find('li', class_="illustrated-features__item--interior"),'text',None)
            
            info =[title,location,price,area,room,furniture]
            thewriter.writerow(info)


        

