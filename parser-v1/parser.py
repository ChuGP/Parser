import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import prettytable as pt
import sys

def addlist(package):
  keywords_list=[]
  for content in package:
    keywords_list.append(content['name'])
  return keywords_list

def adddict(list):
  keywords_dict={}
  for content in list:
    keywords_dict[content] = str(list.count(content))
  return keywords_dict

if __name__ == '__main__':
  sys.argv[1]
  path = './' + sys.argv[1] + '.xml'
  htmlfile = open(path, 'r', encoding='utf-8')
  htmlhandle = htmlfile.read()
  content =BeautifulSoup(htmlhandle, 'xml')

  #爬資料
  In_other_package = content.findAll('kw',attrs={'library':['DCTLibrary','Keywords']})
  In_local_package = content.findAll('kw',attrs={'type':False,'library':False})
  package = In_other_package + In_local_package
  #爬資料

  
  #寫入NewKeywords表格
  keywords = addlist(package) #回傳list
  keywords_dict = adddict(keywords) #回傳dict
  fo = open ( sys.argv[1]+'.txt' , "a+" ) 
  fo.write('\nKEYWORDS AND REUSE TIMES :\n')
  
  for item in keywords_dict:
    # print(item + ' : ' + str(keywords_dict[item]) )
    fo.write( (item + ' : ' + keywords_dict[item] +'\n').encode("utf8").decode("cp950", "ignore"))