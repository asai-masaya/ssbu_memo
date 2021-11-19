# 各ページの好きな文字を好きな文字に置き換える
# https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e
# https://lets-hack.tech/programming/languages/python/beautifulsoup/
from genericpath import isfile
import os,openpyxl
from bs4 import BeautifulSoup
import re

wb=openpyxl.load_workbook('CharaList.xlsx')
s=wb.get_sheet_by_name('html_base')

for i in range(1,s.max_row+1):
  
  t=str(s.cell(i,1).value)
  n=s.cell(i,2).value
  url = "../chara_pages/"+t+".html"
  if not (os.path.isfile(url)):
    continue

  f=open(url,encoding="utf-8_sig")

  data=f.read()
  # print(data[20:24])
  

  # 'image/'を'images/'に置き換えたい場合
  data.replace('image/','images/')
  data=re.sub('image/','images/',data)

  data.replace('試合動画','参考動画')
  data=re.sub('試合動画','参考動画',data)

  

  f=open(url,'w',encoding="utf-8_sig")
  f.write(data)
  f.close()


