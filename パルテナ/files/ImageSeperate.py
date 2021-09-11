# https://tomomai.com/python-opencv-numpy/
import os
import cv2
import os,openpyxl



# 画像読み込み
image = cv2.imread('../image/chara_choice.jpg')
# 画像サイズを調べる（高さ：h 、幅：w）
h, w = image.shape[:2]
nh = 6  # 画像分割数
nw = 13  # 画像分割数
#h = int(h/nh)
#w = int(w/nw)
h_unit = [55,55,55,55,55,55,55]
h_errt = [0,0,0,-1,-1,-1,-1]
h_errb = [0,-1,-1,-1,-2,-2,-2]
w_unit = 96
h_adj = 1
w_adj = 2
# 分割した画像を内包表記でリスト化
c = []
for x in range(nh):
    for y in range(nw):
        c = c + [image[h_adj+h_errt[x] +h_unit[x]*x:h_adj+h_errb[x] + h_unit[x]*(x+1), w_adj + w_unit*y:w_adj + w_unit*(y+1)]]
# c のリストから1つづつ取り出して
# ファイル番号（0.jpg、1.jpg、・・）を付けて、sepaフォルダに保存

x = 6
for y in range(8):
    c = c + [image[h_adj +h_errt[x]+ h_unit[x]*x:h_adj+h_errb[x] + h_unit[x]*(x+1), int(w_unit*2.5) + w_adj + w_unit*y:w_adj + int(w_unit*2.5)+ w_unit*(y+1)]]

wb=openpyxl.load_workbook('CharaList.xlsx')
s=wb.get_sheet_by_name('chara_choice')



for i, img in enumerate(c):
    cv2.imwrite(os.path.join('../image/chara_choice_icon', '{}.png'.format(s.cell(i+1,1).value)), img)
