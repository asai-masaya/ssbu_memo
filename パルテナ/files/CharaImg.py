# 東大柔道部ブログの新しい投稿を50個取得し、excelファイルで出力する
import collections
import requests,bs4,time,openpyxl

url='https://smashmate.net/fighter/'
a=0

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
chara_pages=soup.select('.smashlist a')
for i in range(len(chara_pages)):
  # print(kiji_elems[i].get('title'))
  # print(chara_pages[i].get('href'),chara_pages[i].getText())
  url=chara_pages[i].get('href')
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text,'html.parser')
  chara_icon=soup.select('.smash-icon')
  print(len(chara_icon))
  url=chara_icon[0].get('src')



print('終わり')
