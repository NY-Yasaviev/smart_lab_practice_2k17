import random
import string

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, render, redirect
from .models import *
from .forms import *
from django.contrib.auth import get_user_model


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def ind_list(request):
    edu = IndividualTask.objects.filter(practice_type=IndividualTask.EDU)
    prod = IndividualTask.objects.filter(practice_type=IndividualTask.PROD)
    dip = IndividualTask.objects.filter(practice_type=IndividualTask.DIP)
    return render(request, 'deanery/ind_tasks.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def ind_edit(request, id):
    title = "Редактирование индивидуального задания"
    ind = IndividualTask.objects.get(pk=id)
    if request.POST:
        form = IndividualTaskForm(request.POST or None, instance=ind)
        if form.is_valid():
            form.save()
            return redirect("/ind_tasks/")
        else:
            return render(request, 'deanery/ind_task.html', locals())
    else:
        form = IndividualTaskForm(instance=ind)
        return render(request, 'deanery/ind_task.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_ind(request, type):
    if type == 'edu':
        choice = IndividualTask.EDU
    elif type == 'prod':
        choice = IndividualTask.PROD
    elif type == 'dip':
        choice = IndividualTask.DIP
    else:
        return redirect('/ind_tasks/')
    if request.POST:
        number = IndividualTask.objects.filter(practice_type=choice).count() + 1
        form = IndividualTaskForm(request.POST or None, initial={
            'practice_type': choice,
            'task_number': number
        })
        if form.is_valid():
            form.save()
            return redirect('/ind_tasks/')
        else:
            return render(request, 'deanery/addIndTask.html', {'form': form})
    else:
        form = IndividualTaskForm(initial={
            'practice_type': choice
        })
        return render(request, 'deanery/addIndTask.html', {'form': form})


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
            return redirect("/practices/%s/" % id)
        else:
            return render(request, 'deanery/practice.html', {'form': form})
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
            login = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user = get_user_model().objects.create_user(username=login, password=password)
            Group.objects.get(name='Students').user_set.add(user)
            student.login = login
            student.password = password
            student.user = user
            student.save()
            form.save_m2m()
            return redirect("/students/")
        else:
            return render(request, 'deanery/addStudent.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'deanery/addStudent.html', {'form': form})


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def reports(request, id):
    student = Student.objects.get(pk=id)
    report_list = Report.objects.get(student=student)
    return render(request, 'deanery/reports.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def inds(request, id):
    student = Student.objects.get(pk=id)
    ind_docs = IndividualTaskDoc.objects.get(student=student)
    return render(request, 'deanery/ind_tasks.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def passes(request, id):
    student = Student.objects.get(pk=id)
    passes = Pass.objects.get(student=student)
    return render(request, 'deanery/passes.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def student_report(request, id, rep_id):
    student = Student.objects.get(pk=id)
    group = student.group
    fio = student.name
    practice = Report.objects.get(pk=rep_id).practice
    teacher, director = practice.teacher, practice.director
    return render(request, 'deanery/report.html', locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
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


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def student_pass(request, id, pass_id):
    student = Student.objects.get(pk=id)
    pass_doc = Pass.objects.get(student=student)
    practice = pass_doc.practice
    if request.POST:
        form = PassForm(request.POST or None, instance=pass_doc)
        if form.is_valid():
            form.save()
            return redirect("students/%s/pass/" % id)
    else:
        form = PassForm(instance=pass_doc)
        return render(request, 'deanery/pass.html', locals())


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
