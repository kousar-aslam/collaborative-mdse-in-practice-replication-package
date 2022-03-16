import openpyxl
import csv

def sensitive_data():
    return [(182, 4)]

workbook = openpyxl.load_workbook('../03_data/latest/data.xlsx')
sheet = workbook.active

#Remove sensitive information
for (col, colNum) in sensitive_data():
    sheet.delete_cols(col, colNum)
    
#Save as CSV
with open('../03_data/latest/data.csv', 'w', newline="") as file_handle:
    csv_writer = csv.writer(file_handle, delimiter=';')
    for row in sheet.iter_rows():
        csv_writer.writerow([cell.value for cell in row])