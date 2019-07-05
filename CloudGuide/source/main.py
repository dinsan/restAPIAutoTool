import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Add a number format for cells with money.
money = workbook.add_format({'num_format': '$#,##0'})

# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)
worksheet.write_formula('C1', '=SUM(A1:B1)')

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
index = 1

for item, cost in (expenses):

    index += 1

    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost, money)
    worksheet.write(row, col + 2, cost, money)
    worksheet.write(row, col + 3, '=SUM(B'+str(index)+':C'+str(index)+')', money)
    row += 1

    print(index)

# Write a total using a formula.
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()
