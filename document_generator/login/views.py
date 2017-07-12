from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth


def login(request):
    args = {}
    args.update(csrf(request))
    if not auth.get_user(request).is_authenticated:
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                args['login_error'] = "Пользователь не найден"
                return render_to_response('login/login.html', args)

        else:
            return render_to_response('login/login.html', args)
    else:
        return redirect("/")


def logout(request):
    auth.logout(request)
    return redirect("/")