import requests
from bs4 import BeautifulSoup
url='https://saltnp.com/collections/shirts-blouses?filter.p.product_type=SHIRT&sort_by=manual'
response= requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
shirts =soup.find_all('div', class_='product-block')
for shirt in shirts:
        
        shirt_name = shirt.find('div',class_='product-block__title').text
        price = shirt.find('div', class_='product-price').span.text
        price=float(price.replace('Rs','').replace(',','')) #converting the string into a numerical value
        color= shirt.find('span', class_='product-block-options__item__text').text
        
    
        if price<2500:
            print(f'''
              
              Shirt name: {shirt_name}
              Price of the piece: {price}
              Color: {color}
              

            ''')