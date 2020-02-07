from requests import get
from bs4 import BeautifulSoup as soup

url='https://www.flipkart.com/search?q=iphone+11+pro+camera&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_0_6_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_0_6_na_na_na&as-pos=0&as-type=HISTORY&suggestionId=iphone+11+pro+camera%7CMobiles&requestId=8c54d4ce-3e9d-4d35-8dbd-c4e12fbaa833&as-searchtext=iphone'
response=get(url)
print(response)

html_soup=soup(response.text,'html.parser')
print(type(html_soup))
print(html_soup)
    
iphone_container=html_soup.find_all('div',class_='_3O0U0u')
print(len(iphone_container))
print(soup.prettify(iphone_container[0]))


iphone=iphone_container[0]
print(iphone_container.div.img['alt'])
