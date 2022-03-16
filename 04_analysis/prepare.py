import openpyxl
import csv

def sensitive_data():
    return [(182, 4)]

fileLocation = '../03_data/latest'
    
workbook = openpyxl.load_workbook('{}/data.xlsx'.format(fileLocation))
sheet = workbook.active

#Remove sensitive information
for (col, colNum) in sensitive_data():
    sheet.delete_cols(col, colNum)
    
#Save as CSV
with open('{}/data.csv'.format(fileLocation), 'w', newline="") as file_handle:
    csv_writer = csv.writer(file_handle, delimiter=';')
    for row in sheet.iter_rows():
        csv_writer.writerow([cell.value for cell in row])