"""
URL configuration for xmutplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

import groups.views
import verify.views
from . import views

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)
def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('', views.index),
    path('bot', views.bot),
    path('verify', views.verify),
    path('verify/qq', verify.views.qq),
    path('verify/generate', verify.views.generate),
    path('verify/logout', verify.views.logoutForm),
    path('verify/authorizes', verify.views.authorizes),
    path('groups', groups.views.index),
    path('website', groups.views.website, name="website"),
    path('calendar', groups.views.calendar, name="calendar.html"),
    path('disclaimer', views.disclaimer),
    re_path(r'^favicon\.ico$', favicon_view),
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
]
