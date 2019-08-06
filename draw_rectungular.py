import cv2, glob, os
import matplotlib.pyplot as plt
import xlrd
import xlsxwriter

path = 'dataset_label.xlsx'
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(3)

coor = -1
index = 5
for i in range(sheet.nrows):
    coor0 = sheet.cell_value(i, 0)
    if coor0 == 'Image':
        continue
    # if coor0 != 'scene'+str(index):
    #     continue
    # if coor0 == 'scene'+str(index+2):
    #     break
    # coor1 = int(sheet.cell_value(i, 1))
    coor0 = int(sheet.cell_value(i, 0))
    x = int(sheet.cell_value(i, 1))
    y = int(sheet.cell_value(i, 2))
    w = int(sheet.cell_value(i, 3))
    h = int(sheet.cell_value(i, 4))
    #path0 = '/home/ziyi/Documents/test_label/test/Scene'+str(index)+'/Delete/Delete'+str(index)+'_One-Face' + str(coor1) + '.png'
    # path0 = '/home/ziyi/Documents/test_label/test/Scene' + str(index) + '/Delete/Delete' + str(coor1) + '.png'
    imagePath = '/home/ziyi/Documents/test_label/Delete/Delete' + str(coor0) + '.png'
    path0 = '/home/ziyi/Documents/test_label/test/Delete/Delete' + str(coor0) + '.png'
    # if coor == coor1:
    #     imagePath = path0
    # else:
    #     imagePath = '/home/ziyi/Documents/test_label/Scene'+str(index)+'/Delete/Delete'+str(coor1)+'.png'

    image = cv2.imread(imagePath)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite(path0, image)
    # coor = coor1






