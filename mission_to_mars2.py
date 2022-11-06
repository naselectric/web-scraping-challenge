from bs4 import BeautifulSoup
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager





executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

URL ='https://redplanetscience.com'

browser.visit(URL)

html = browser.html
soup = BeautifulSoup(html,'lxml')
Dates = soup.find_all('div',{'class':'list_date'})
News_titles=soup.find_all('div',{'class':'content_title'})
News_teasers=soup.find_all('div',{'class':'article_teaser_body'})

datelist={'date':[]}
titlelist={'title':[]}
newslist={'news':[]}

i=-1
for Date in Dates:
        i=i+1
        datelist['date'].append(Date.text)
        titlelist['title'].append(News_titles[i].text)
        newslist['news'].append(News_teasers[i].text)



URL2='https://spaceimages-mars.com'

browser.visit(URL2)

html2 = browser.html

soup2= BeautifulSoup(html2,'lxml')

image = soup2.find('img',{'class':'headerimage fade-in'})

featured_image2=URL2 +'/'+ image['src']

image1={'image1':[featured_image2]}



URL4='https://marshemispheres.com'
URL5='https://marshemispheres.com/cerberus.html'
URL6='https://marshemispheres.com/schiaparelli.html'
URL7='https://marshemispheres.com/syrtis.html'
URL8='https://marshemispheres.com/valles.html'

URLS=[URL5,URL6,URL7,URL8]

for url in URLS:
    browser.visit(url)
    html_mars=browser.html
    hemisoup=BeautifulSoup(html_mars,'lxml')
    hemi_image=hemisoup.find('img',{'class':'wide-image'})
    im1=hemi_image['src']
    hemi_image1=URL4+'/'+im1
    image1['image1'].append(hemi_image1)

def dates():
    return datelist

def titles():
        return titlelist

def news():
        return newslist

def first_image():
        return image1        





