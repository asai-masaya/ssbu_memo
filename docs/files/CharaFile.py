import os

# path=os.path.relpath('../chara/')

# for i in range(1,91):
#   file=open(str(i)+'.html','w')
#   file.close

# ↓最新版

# 各キャラページのテンプレートを作る
from genericpath import isfile
import os,openpyxl,shutil

wb=openpyxl.load_workbook('CharaList.xlsx')
s=wb.get_sheet_by_name('Sheet1')

for i in range(2,s.max_row+1):
  if(i==9):
    continue
  
  t=str(s.cell(i,1).value)
  n=s.cell(i,2).value
  url="../chara_page/"+t+".html"
  # print(url)
  if(os.path.isfile(url)):
    shutil.copy("../chara_page/01.html","../chara_page/"+t+".html")

