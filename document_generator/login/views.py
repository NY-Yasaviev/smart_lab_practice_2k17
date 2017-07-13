from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import Group, User


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user in Group.objects.get_by_natural_key("Students"):
                return redirect('students/')
            elif request.user in Group.objects.get_by_natural_key("Deanery"):
                return redirect('deanery/')
            else:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login/login.html', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login/login.html', args)

    else:
        return render_to_response('login/login.html', args)


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")