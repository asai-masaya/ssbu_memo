import os

path=os.path.relpath('../chara/')

for i in range(1,91):
  file=open(str(i)+'.html','w')
  file.close