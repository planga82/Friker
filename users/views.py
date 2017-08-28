# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout1(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('photos_home')

def login1(request):
    return render(request,'users/login.html')


