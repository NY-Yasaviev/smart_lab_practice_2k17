from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import Group, User
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
                return render_to_response('student/index.html')
            elif request.user.groups.get().name == "Deanery":
                practices = Practice.objects.all()[:5]
                students = Student.objects.all()[:10]
                return render(request, 'deanery/index.html', locals())
            else:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login/login.html', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login/login.html', args)

    else:
        if auth.get_user(request).is_authenticated:
            if request.user.groups.get().name == "Students":
                return render_to_response('student/index.html')
            elif request.user.groups.get().name == "Deanery":
                practices = Practice.objects.all()[:5]
                students = Student.objects.all()[:10]
                return render(request, 'deanery/index.html', locals())
        else:
            return render_to_response('login/login.html', args)


def logout(request):
    if auth.get_user(request).is_authenticated:
        auth.logout(request)
    return redirect('/')
