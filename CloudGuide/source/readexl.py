# Program to extract number of
# columns in Python
import xlrd

loc = ("hello.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(1, 1)

for i in range(sheet.nrows):
    print(sheet.cell_value(i, 3))