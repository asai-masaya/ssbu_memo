# Javascriptを作成するためのファイル
import os,openpyxl

f=open('ForRondom.txt','w')
wb=openpyxl.load_workbook('CharaList.xlsx')
s=wb.get_sheet_by_name('html_base')


txt="\"./chara_page/01.html\""

for i in range(2,81):
  url=str(s.cell(i,1).value)
  txt=txt+', \"./chara_page/'+str(s.cell(i,1).value)+'.html\"'
  print(i)
  "./chara_page/01.html"

f.write(txt)
f.close()