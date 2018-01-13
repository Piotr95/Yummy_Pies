# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from UserManagement.forms import  Registration_Form


def index(request):
     if request.user.is_authenticated():
      return render(request, 'Home/authindex.html')

     return render(request,'Home/index.html')
from django.contrib.staticfiles import finders



# Create your views here.
