# スマメイトからキャラリストを持ってくる
import collections
import requests,bs4,time,openpyxl

url='https://www.smashbros.com/ja_JP/fighter/index.html'

print(1)


file=open("CharaList.txt","w")
file.truncate(0)


res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
charaname=soup.select('.fighter-list__name-main')
charanum=soup.select('.fighter-list__num-txt')
print(len(charaname))
print(len(charanum))
for i in range(len(charaname)):
  file.write(charanum[i]+' '+charaname[i]+'\n')

file.close

print('終わり')

