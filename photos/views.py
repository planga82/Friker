# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from photos.models import photo, PUBLIC


def home(request):
    photos = photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list':photos[:2]
    }
    return render(request,'photos/home.html',context)

