import xlrd
from .models import Details, Academics, sports, extra_curricular

def parse_excel(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    student_data = dict()
    for row in range(1, sheet.nrows):
        for col in range(0,sheet.ncols):
            cell_value_key = sheet.cell(0, col).value
            if type(cell_value_key)== str:
                cell_value_key = '_'.join(str.lower(cell_value_key).split(' '))

            cell_value = sheet.cell(row, col).value

            student_data[cell_value_key] = cell_value



