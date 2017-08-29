# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm

from photos.models import photo, PUBLIC


def home(request):
    photos = photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list':photos[:2]
    }
    return render(request,'photos/home.html',context)

def detail(request, pk):
    """
    Carga la pagina de detalle de una foto
    :param request: HTTPRequuest
    :param pk: id photo
    :return httpresponse
    """
    posible_photo = photo.objects.filter(pk=pk)

    photo0 = posible_photo[0] if len(posible_photo) == 1 else None
    if photo0 is not None:
        context = {
            'photo' : photo0
        }
        return render(request,'photos/detail.html',context)
    else:
        return HttpResponseNotFound('No existe la foto')

def create(request):
    """
    Muestra un formulario para crear la foto
    :param request:
    :return:
    """
    form = PhotoForm()
    context = {
        'form' : form
    }
    return render(request, 'photos/new_photo.html', context)
