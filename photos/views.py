# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from photos.models import photo


def home(request):
    photos = photo.objects.all()
    html = '<ul>'
    for photoO in photos:
        html += '<li>' + photoO.name + '</li>'
    html += '</ul>'
    return HttpResponse(html)

