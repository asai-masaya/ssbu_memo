# 各ページの好きな文字を好きな文字に置き換える
# https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e
# https://lets-hack.tech/programming/languages/python/beautifulsoup/
from genericpath import isfile
import os,openpyxl
from bs4 import BeautifulSoup
import re

wb=openpyxl.load_workbook('CharaList.xlsx')
s=wb.get_sheet_by_name('Sheet1')

for i in range(2,s.max_row+1):
  
  t=str(s.cell(i,1).value)
  n=s.cell(i,2).value
  url = "../chara_page/"+t+".html"
  if not (os.path.isfile(url)):
    continue

  f=open(url,encoding="utf-8_sig")

  data=f.read()
  # print(data)
  
  data.replace('image/','images/')
  # data.replace('01',t)

  data=re.sub('image/','images/',data)
  # data=re.sub('01',t,data)

  f=open(url,'w',encoding="utf-8_sig")
  f.write(data)
  f.close()


