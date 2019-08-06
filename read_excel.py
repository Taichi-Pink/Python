import pandas as pd
import xlrd
import xlsxwriter

path = 'dataset_one_label.xlsx'
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
writer = xlsxwriter.Workbook('label_one.xlsx')
work_sheet = writer.add_worksheet()

for i in range(sheet.nrows):
    coor = sheet.cell_value(i,1)
    x = coor.split("[",1)
    x = x[1].split("]", 1)
    x = x[0].split(",", 3)
    work_sheet.write('A'+str(i), x[0])
    work_sheet.write('B'+str(i), x[1])
    work_sheet.write('C'+str(i), x[2])
    work_sheet.write('D'+str(i), x[3])

writer.close()



