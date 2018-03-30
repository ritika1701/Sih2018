import xlrd, datetime, os
from .models import Details, School, Academics, sports, extra_curricular


def parse_excel(filename='sih_excel', schoolcode='AKG_067'):

    wb = xlrd.open_workbook(os.getcwd()+'/dashboard/excels/' + filename + '.xlsx')
    sheet = wb.sheet_by_index(0)

    student_data = dict()
    for row in range(1, sheet.nrows):
        for col in range(0, sheet.ncols):
            cell_value_key = str.lower(sheet.cell(0, col).value)
            cell_value = sheet.cell(row, col).value
            print("cell_""cell value-",cell_value)
            if 'dob' in cell_value_key:
                cell_value = ''.join(cell_value.split('_'))
                cell_value = ''.join(cell_value.split('/'))
                cell_value = datetime.datetime.strptime(cell_value, "%d%m%Y").date()
                student_data['dob'] = cell_value

            elif cell_value_key == "Sports" or cell_value_key=="Extra Curricular":
                if cell_value is '':
                    continue
                else:
                    print(cell_value)
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
        print(student_data,school)
        student = Details(rollno=student_data['rollno'],student_name=student_data['student_name'],school=school,grade=student_data['grade'],acad_year=student_data['acad_year'],gender=student_data['gender'],dob = student_data['dob'],teacher_remark=student_data['teacher_remark'],preferred=student_data['preferred'])
        # student.save()