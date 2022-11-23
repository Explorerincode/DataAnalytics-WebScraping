from bs4 import BeautifulSoup
import requests
url = "https://www.pararius.com/apartments/delft"
page =requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
lists= soup.find_all('section', class_="listing-search-item")

for list in lists:
    title = lists.find('a', class_="listing-search-item__link--title")
    location = lists.find('div', class_="listing-search-item__sub-title")
    price = lists.find('div', class_="listing-search-item__price")
    area = lists.find('li', class_="illustrated-features__item--surface-area")
    room = lists.find('li', class_="illustrated-features__item--number-of-rooms")
    furniture = lists.find('li', class_="illustrated-features__item--interior")
  
    info =[title,location,price,area,room,furniture]
    print(info)

