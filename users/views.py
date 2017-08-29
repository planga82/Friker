# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth import logout as django_logout,authenticate, login as django_login
from django.shortcuts import redirect, render
from forms import LoginForm

def logout1(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('photos_home')

def login1(request):


    error_messeges = []

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #username = request.POST.get('usr','')
            #password = request.POST.get('pwd','')
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(request, username=username, password=password)
            if user is None:
                error_messeges.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request,user)
                    return redirect('photos_home')
                else:
                    error_messeges.append('El usuario no esta activo')
    else:
        form = LoginForm()
    context = {
        'errors' : error_messeges,
        'login_form' : form
    }
    return render(request, 'users/login.html',context)



