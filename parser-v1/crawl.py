import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re

def get_page_content(URL):
    res = requests.get(
    	url=URL,
        cookies={'over18':'1'}
    )
    content = BeautifulSoup(res.text,'html.parser')
    return content

soup = get_page_content('https://www.ptt.cc/bbs/Gossiping/index39076.html')
print(soup)
print("success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
soup2 = get_page_content('https://www.ptt.cc/bbs/Gossiping/index39075.html')
print(soup)
#使用迴圈進入到目標頁面中的每個主題頁面

# for article in soup.select('.r-ent a'):
#     url = 'https://www.ptt.cc' + article['href']
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
    
#     #判斷網址中有沒有圖片，如果有就開始下載
#     gp = re.compile('http:\/\/i\.imgur\.com\/.*')
#     if len(soup.findAll('a', {'href':gp})) > 0:
#         for index, img_url in enumerate(soup.findAll('a', {'href':gp})):
#             try:
#                     #記得更改想要下載到的位置
#                 urlretrieve(img_url['href'], '.\{}_{}_.jpg'.format(article.text, index))
#             except:
#                 print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], article.text, index))
#             break