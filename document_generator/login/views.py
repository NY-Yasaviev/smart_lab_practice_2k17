from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import Group, User

from generator.forms import StudentForm
from generator.models import *


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.groups.get().name == "Students":
                title = "Главная"
                student = Student.objects.get(user=request.user)
                form = StudentForm(request.POST or None, instance=student)
                if form.is_valid():
                    form.save()
                return redirect("/")
            elif request.user.groups.get().name == "Deanery":
                title = "Главная"
                practices = Practice.objects.all()[:5]
                students = Student.objects.all()[:10]
                return render(request, 'deanery/index.html', locals())
            else:
                title = "Авторизация"
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login/login.html', args)
        else:
            title = "Авторизация"
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login/login.html', args)

    else:
        if auth.get_user(request).is_authenticated:
            if request.user.groups.get().name == "Students":
                title = "Главная"
                student = Student.objects.get(user=request.user)
                form = StudentForm(instance=student)
                practices = Practice.objects.filter(student=student)
                return render(request, 'student/index.html', locals())
            elif request.user.groups.get().name == "Deanery":
                title = "Главная"
                practices = Practice.objects.all()[:5]
                students = Student.objects.all()[:10]
                return render(request, 'deanery/index.html', locals())
        else:
            title = "Авторизация"
            return render_to_response('login/login.html', args)


def logout(request):
    if auth.get_user(request).is_authenticated:
        auth.logout(request)
    return redirect('/')
