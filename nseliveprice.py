import requests
from requests import get
from bs4 import BeautifulSoup 


stock_symbol ='reliance'
url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol'+stock_symbol
response = get(url)

html_soup = BeautifulSoup(resonse.text,'html.parser')
print(htm_soup)
