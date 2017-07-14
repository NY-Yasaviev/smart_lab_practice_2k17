import random
import string

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, render, redirect
from .models import *
from .forms import *
from django.contrib.auth import get_user_model


def edit_report(request):
    pass


def edit_pass(request):
    pass


def edit_individual(request):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_practice(request):
    if request.POST:
        form = PracticeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/practices/")
    else:
        form = PracticeForm()
        return render(request, 'deanery/addPractice.html', {'form': form})


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def edit_practice(request, id):
    practice = Practice.objects.get(pk=id)
    if request.POST:
        form = PracticeForm(request.POST or None, instance=practice)
        if form.is_valid():
            form.save()
            return redirect("/practices/%s/" % id)
    else:
        form = PracticeForm(instance=practice)
        return render(request, 'deanery/practice.html', {'form': form}, locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def new_student(request):
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
        form = StudentForm()
        return render(request, 'deanery/addStudent.html', {'form': form})


def student_report(request, id):
    pass


def student_individual(request, id):
    pass


def student_pass(request, id):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def edit_student(request, id):
    student = Student.objects.get(pk=id)
    if request.POST:
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/students/%s/" % id)
    else:
        form = StudentForm(instance=student)
        return render(request, 'deanery/student.html', {'form': form}, locals())


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def practices(request):
    practices_list = Practice.objects.all()
    return render(request, 'deanery/practices.html', locals())


def edit_diary(request):
    pass


@user_passes_test(lambda u: Group.objects.get(name='Deanery') in u.groups.all())
def students(request):
    students_list = Student.objects.all()
    return render(request, 'deanery/students.html', locals())
