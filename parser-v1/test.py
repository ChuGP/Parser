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

html =  get_page_content('https://www.ptt.cc/bbs/Gossiping/index39076.html')
rows = html.findAll('div',{'class':'r-ent'})

posts = list()
	
for row in rows:
    meta = row.find('div', 'title').find('a')
    if meta :    # 如果文章已被刪除，meta 會是 None
        posts.append({
            'link': meta['href'],                         # 文章網址
            'title': meta.text,                           # 文章標題
            'date': row.find('div', 'date').text,     # 文章發布日期
            'author': row.find('div', 'author').text, # 文章作者
            'push': row.find('div', 'nrec').text      # 推文數
        })

fo = open ( "test.txt" , "a+" ) 
for gp in posts:
  fo.write ( 'link: '+gp['link'] ) 
  fo.write ( 'title: ' + gp['title']+'\n' ) 
  fo.write ( 'date: ' + gp['date']+'\n' ) 
  fo.write ( 'author: ' + gp['author']+'\n' ) 
  fo.write ( 'push: ' + gp['push']+'\n' ) 
  fo.write ( '------------------------------------------------------------------------------'+'\n' )
  print(gp)
fo . close ()

fo = open ( "test.txt" , "a+" ) 
fo.write("test")