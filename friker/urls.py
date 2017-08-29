"""friker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from photos import views as photoviews
from users import views as userviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Photos urls
    url(r'^$', photoviews.home,name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', photoviews.detail, name='photo_detail'),
    url(r'^photos/new$', photoviews.create, name='create_photo'),

    #Users Urls
    url(r'^login$', view=userviews.login1 , name='user_login', ),
    url(r'^logout$', view=userviews.logout1, name='user_logout')
]
