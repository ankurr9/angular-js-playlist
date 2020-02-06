
from requests import get
from bs4 import BeautifulSoup

url ='https://www.amazon.in/s?k=iphones&ref=nb_sb_noss_2'
response =get(url)

html_soup=BeautifulSoup(response.text,'html.parser')
print(html_soup)

iphone_names =html_soup.find_all('div',class_="a-section a-spacing-none")
print(iphone_names)


# lists to store the scrapped data

names =[]
price =[]

for iphonenamess in iphone_names:
    if iphonenamess.find('div' ,class_="a-link-normal a-text-normal"):
        print(iphonenamess)

        name =iphonenamess.div.span.text
        names.append(name)
        print(names)
