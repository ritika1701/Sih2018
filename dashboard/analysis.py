from django.db.models import Max, Min, FloatField, Avg
from .models import Academics, sports, extra_curricular, Details, School


def get_academic_performance(grade=2, subject='eng', cutoff=92):
    students_data = Academics.objects.filter(student__grade=grade).filter(student__preferred__icontains='academics')
    min_sub_marks = students_data.aggregate(Min(subject, output_field=FloatField()))[subject + '__min']
    max_sub_marks = students_data.aggregate(Max(subject, output_field=FloatField()))[subject + '__max']
    score_list = []
    for student in students_data:
        student_subject_marks = getattr(student, subject)
        try:

            normalized_score = 1000 * (student_subject_marks - min_sub_marks) / (max_sub_marks - min_sub_marks)
        except ZeroDivisionError:
            normalized_score = 1000
        score_list.append((student.student, normalized_score))
    sorted(score_list, key=lambda x: x[1])
    try:

        cutoff = 1000 * (cutoff - min_sub_marks) / (max_sub_marks - min_sub_marks)
    except ZeroDivisionError:
        cutoff = 1000
    student_list = [x[0] for x in score_list if x[1] >= cutoff]
    return student_list


def get_sports_performance(grade=2, sport_name='badminton', cutoff=7):
    students_data = sports.objects.filter(student__grade=grade).filter(sport_name__iexact=sport_name).filter(
        student__preferred__icontains='sports')
    score_list = []
    for student in students_data:
        sport_score = (student.semi / student.matches) * 2 + (student.final / student.semi) * 3 + (
                student.won / student.final) * 5
        s = sports.objects.get(sport_name=sport_name, student=student.student, student__grade=grade)
        s.sport_score = round(sport_score, 2)
        s.save()


    students_data = sports.objects.filter(student__grade=grade).filter(sport_name__iexact=sport_name).filter(
        student__preferred__icontains='sports')
    min_sport_score = students_data.aggregate(Min('sport_score', output_field=FloatField()))['sport_score__min']
    max_sport_score = students_data.aggregate(Max('sport_score', output_field=FloatField()))['sport_score__max']

    for student in students_data:
        try:
            normalized_score = 1000 * (student.sport_score - min_sport_score) / (max_sport_score - min_sport_score)
        except ZeroDivisionError:
            normalized_score = 10
        score_list.append((student.student, normalized_score))

    sorted(score_list, key=lambda x: x[1])
    student_list = [x[0] for x in score_list if x[1] >= cutoff]
    return student_list


def get_extracurricular_performance(grade=2, activity_name='music', cutoff=7):
    students_data = extra_curricular.objects.filter(student__grade=grade).filter(
        activity_name__iexact=activity_name).filter(
        student__preferred__icontains='others')
    score_list = []

    for student in students_data:
        e = extra_curricular.objects.get(student__grade=grade, activity_name__iexact=activity_name, student=student.student)
        activity_score = (student.intra_won / student.intra_played) * 4 + (
                student.inter_won / student.inter_played) * 6
        e.activity_score = round(activity_score,2)
        e.save()

    min_activity_score = students_data.aggregate(Min('activity_score', output_field=FloatField()))[
        'activity_score__min']
    max_activity_score = students_data.aggregate(Max('activity_score', output_field=FloatField()))[
        'activity_score__max']

    students_data = extra_curricular.objects.filter(student__grade=grade).filter(
        activity_name__iexact=activity_name).filter(
        student__preferred__icontains='others')

    for student in students_data:
        try:
            normalized_score = 1000 * (student.activity_score - min_activity_score) / (
                    max_activity_score - min_activity_score)
        except ZeroDivisionError:
            normalized_score = 1000
        score_list.append((student.student, normalized_score))

    sorted(score_list, key=lambda x: x[1])
    student_list = [x[0] for x in score_list if x[1] >= cutoff]
    return student_list

# Smart Suggestions
# def give_suggestion(grade=2,domain='academics',sub_domain='eng'):
#     if domain is 'academics':
#
#         student_data = Academics.objects.filter(student__grade=grade).aggregate(Avg(sub_domain))
#
#     elif domain is 'sports':
#         students = sports.objects.filter(sport_name__iexact=sub_domain).filter(student__grade=grade)
#         for student in students:
#
#             sport_score = (student.semi / student.matches) * 2 + (student.final / student.semi) * 3 + (
#                     student.won / student.final) * 5
#             s = sports.objects.get(sport_name=sub_domain, student=student.student, student__grade=grade)
#             s.sport_score = round(sport_score, 2)
#             s.save()



