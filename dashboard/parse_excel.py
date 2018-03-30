import xlrd
from .models import Details, School, Academics, sports, extra_curricular


def parse_excel(filename, schoolcode):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    student_data = dict()
    for row in range(1, sheet.nrows):
        for col in range(0, sheet.ncols):
            cell_value_key = sheet.cell(0, col).value
            cell_value = sheet.cell(row, col).value
            if cell_value_key == "Sports":

                sports_list = cell_value.split(',')
                sport_details = dict()
                for sport in sports_list:
                    sport = sport.split(' ')
                    sport_details[sport[0]] = sport[1:]

                student_data['sports'] = sport_details
            else:
                cell_value_key = '_'.join(str.lower(cell_value_key).split(' '))
                student_data[cell_value_key] = cell_value

    school = School.objects.get(schoolcode=schoolcode)

    Details.create()