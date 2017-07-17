import random
import string

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, render, redirect
from .models import *
from .forms import *
from django.contrib.auth import get_user_model


def ind_edit(request, id):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def ind_list(request):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_ind(request, type):
    pass


def edit_report(request):
    pass


def edit_pass(request):
    pass


def edit_individual(request):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_practice(request):
    title = "Добавление практики"
    if request.POST:
        form = PracticeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/practices/")
        else:
            return render(request, 'deanery/addPractice.html', {'form': form})
    else:
        form = PracticeForm()
        return render(request, 'deanery/addPractice.html', {'form': form})


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def edit_practice(request, id):
    title = "Редактирование практики"
    practice = Practice.objects.get(pk=id)
    # students_list = Student.objects.get(practice=practice)
    students_list = Student.objects.all().filter(practice=practice)
    if request.POST:
        form = PracticeForm(request.POST or None, instance=practice)
        if form.is_valid():
            form.save()
        return redirect("/practices/")
    else:
        form = PracticeForm(instance=practice)
        return render(request, 'deanery/practice.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_student(request):
    title = "Добавление студента"
    if request.POST:
        form = StudentForm(request.POST or None)
        if form.is_valid():
            student = form.save(commit=False)
            for practice in student.practice.objects.all():
                diary = DiaryForm(student=student, practice=practice)
                diary.save()
            login = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user = get_user_model().objects.create_user(username=login, password=password)
            Group.objects.get(name='Students').user_set.add(user)
            student.login = login
            student.password = password
            student.user = user
            student.save()
            form.save_m2m()
            # creating docs
            pass_doc = Pass.objects.create()
            return redirect("/students/")
    else:
        form = StudentForm()
        return render(request, 'deanery/addStudent.html', {'form': form})


def reports(request, id):
    pass


def inds(request, id):
    pass


def passes(request, id):
    pass


def student_report(request, id, rep_id):
    student = Student.objects.get(pk=id)
    group = student.group
    fio = student.name
    practice = Report.objects.get(pk=rep_id).practice
    teacher, director = practice.teacher, practice.director
    return render(request, 'deanery/report.html', locals())


def student_individual(request, id, ind_id):
    doc = IndividualTaskDoc.objects.get(pk=ind_id)
    records = IndividualTask.objecs.get(doc=doc)
    practice = doc.practice
    student = doc.student
    fio = student.name
    edu_profile = student.edu_profile
    place_of_practice, date_from, date_to, director = \
        practice.company, practice.date_from, practice.date_to, practice.director
    return render(request, 'deanery/individual.html', locals())


def student_pass(request, id, pass_id):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def edit_student(request, id):
    title = "Редактирование студента"
    student = Student.objects.get(pk=id)
    if request.POST:
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/students/")
    else:
        form = StudentForm(instance=student)
        return render(request, 'deanery/student.html', {'form': form}, locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def practices(request):
    title = "Практики"
    practices_list = Practice.objects.all()
    return render(request, 'deanery/practices.html', locals())


def edit_diary(request):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def students(request):
    title = "Студенты"
    students_list = Student.objects.all()
    return render(request, 'deanery/students.html', locals())


def diary_view(request):
    return render(request, 'student/diaryView.html', locals())


def report_view(request):
    return render(request, 'student/reportView.html', locals())


def individual_view(request):
    pass


def pass_view(request):
    return render(request, 'student/passView.html', locals())


def practice_docs(request):
    pass
