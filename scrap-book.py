# 引入所需模块
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import json
#调用Chrome或者PhantomJS
driver = webdriver.Chrome()
#driver = webdriver.webdriver.PhantomJS()
#主机
next='https://search.jd.com/Search?keyword=python'
#使用driver获取网页
driver.get(next)
booksstore=[]
#保存数据
fi=open("books.txt","a",encoding='utf-8')
for j in range(4):
    #driver控制滚轮滑动
    for i in range(2):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #等待页面加载完毕
        time.sleep(4)
    content=driver.page_source
    #使用soup查找元素
    eles=soup(content,'html.parser')
    books=eles.find_all('li',{'class':'gl-item'})
    print(len(books))
    for book in books:
        name=book.find('div',{'class':'p-name'}).find('a').find('em').getText()
        price=book.find('div',{'class':'p-price'}).find('i').getText()
        commit='https:'+book.find('div',{'class':'p-commit'}).find('a')['href']
        shop=book.find('div',{'class':'p-shopnum'}).find_all('a')
        print(name)
        print(price)
        print(commit)
        book={'书籍名称':name,'书籍价格':price,'购买地址':commit}
        if(len(shop)!=0):
            shopaddress=shop[0]['href']
            shopname=shop[0]['title']
            print("http:"+shopaddress)
            print(shopname)
            book['商店地址']="http:"+shopaddress
            book['商店名称']=shopname
        
        booksstore.append(book)
        #booksstore.append('\n')
        fi.write(json.dumps(book,ensure_ascii=False))
        fi.write("\n")
    #下一页
    next=driver.find_element_by_class_name('pn-next')
    print(next.text)
    next.click()
    time.sleep(4)

print(len(booksstore))
print(booksstore)
fi.write
fi.close()