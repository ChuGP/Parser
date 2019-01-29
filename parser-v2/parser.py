from bs4 import BeautifulSoup
import re
import prettytable as pt
import sys
import time

def addlist(package):
  keywords_list=[ content['name'] for content in package]
  return list(set(keywords_list) )  #把keyword加進list 

def namedict(contents):
  name_dict={}
  for content in contents:
     if "TMD" in content['name']:name_dict[content['name'].split(' ', 1 )[0]] = content['name']
  return name_dict

def keyword_dict(name_dict,original): 
  Keyword_save = {}
  for item in name_dict:
    temp = original.find('suite',{'name':name_dict[item]}) 
    package = temp.findAll('kw',attrs={'library':['DCTLibrary','Keywords']}) + temp.findAll('kw',attrs={'type':False,'library':False})
    Keyword_save[item] = addlist(package)
  return Keyword_save

def get_master_keyword(Keyword_save,test_case_name):
  default=()
  for item in Keyword_save: 
    if ( item != test_case_name ): default = ( set(default) | set(Keyword_save[item] ) )
  return list (default)

def draw_table(test_case_name,keywords,mark):
  tb = pt.PrettyTable()
  fo = open ( test_case_name +'.txt' , "a+" ) 
  fo.write( '\n' + test_case_name + ' ' + mark + ' KEYWORDS :\n')
  tb.field_names = ["KEYWORDS NAME"]
  if( len(keywords) == 0 ):tb.add_row(['NAN'])
  for ans in keywords: tb.add_row([ans])
  fo.write(str(tb).encode("utf8").decode("cp950", "ignore") + '\n\n')
  fo.close()

if __name__ == '__main__':
  start = time.time()
  path = './' + sys.argv[1] + '.xml'
  test_case_name = sys.argv[2] #要分析的TMD-XXX
  htmlfile = open(path, 'r', encoding='utf-8')
  htmlhandle = htmlfile.read()
  original = BeautifulSoup(htmlhandle,'xml')
  #抓TEST CASE NAME
  contents = original.findAll('suite',attrs={'name':True})
  name_dict = namedict(contents) #做名字的dict key為縮寫 value為全名
  Keyword_save = keyword_dict(name_dict,original) #做keyword的dict key為TMD-XXX value用到的keyword list
  default = get_master_keyword(Keyword_save,test_case_name) #可以reuse的keyword
  new_keywords = list( (set( Keyword_save[test_case_name] ) | set( default ) ) - set( default )  )  #set list轉換為了優化set比較快
  reuse_keywords = list( set( Keyword_save[test_case_name] ) - set( new_keywords ) )
  #做表格
  draw_table(test_case_name,new_keywords,"NEW")
  draw_table(test_case_name,reuse_keywords,"REUSE")
  end = time.time()
  elapsed = end - start
  print ("Time : ", elapsed, "seconds.")