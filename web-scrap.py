# 引入所需模块
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless') #This line should be uncommented if you're using Docker
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#调用Chrome或者PhantomJS
driver = webdriver.Chrome()
#driver = webdriver.webdriver.PhantomJS(options = chrome_options)
#主机
host='http://quotes.toscrape.com'
biaoyus=[]
next='http://quotes.toscrape.com/js/'
for i in range(4):
    #使用driver获取网页
    driver.get(next)
    content=driver.page_source
    #使用soup查找元素
    eles=soup(content,'html.parser')
    biaoyus.append(eles.find_all("div",{"class":"quote"}))
    print(len(biaoyus))
    next=host+eles.find('li',{'class':'next'}).find('a')['href']
    print(next)
    #input()

for biaoyu in biaoyus:
    for quote in biaoyu:
        print(quote.find(class_='text').getText())
        print(quote.find(class_='author').getText())
        print(quote.find(class_='tags').getText())
        print('\n')
