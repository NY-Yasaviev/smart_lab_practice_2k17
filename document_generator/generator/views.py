from django.shortcuts import render_to_response, render,redirect
from .models import *
from .forms import *


def edit_report(request):
    pass


def edit_pass(request):
    pass


def edit_individual(request):
    pass


def new_practice(request):
    pass


def edit_practice(request, id):
    practice = Practice.objects.get(pk=id)
    if request.POST:
        form = PracticeForm(request.POST or None, instance=practice)
        if form.is_valid():
            form.save()
            return redirect("/practices/%s/" % id)
    else:
        form = PracticeForm()
        return render(request, 'deanery/practice.html', {'form': form}, locals())


def new_student(request):
    pass


def student_report(request, id):
    pass


def student_individual(request, id):
    pass


def student_pass(request, id):
    pass


def edit_student(request, id):
    student = Student.objects.get(pk=id)
    if request.POST:
        form = StudentForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/students/%s/" % id)
    else:
        form = StudentForm()
        return render(request, 'deanery/student.html', {'form': form}, locals())


def practices(request):
    practices = Practice.objects.all()
    return render(request, 'deanery/practices.html', locals())


def edit_diary(request):
    pass


def students(request):
    students = Student.objects.all()
    return render(request, 'deanery/students.html', locals())
