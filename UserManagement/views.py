# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate,logout
from UserManagement.forms import  Registration_Form,UserLoginForm
from django.contrib import auth


def register(request):
    form = Registration_Form(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.clean_password2()

        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)

                return render(request, 'Home/authindex.html')
    context = {
        "form": form,
    }
    return render(request, 'UserManagement/register.html', context)

def login(request):

            if request.method == 'POST':
                form=UserLoginForm(request.POST)
                username = request.POST.get('username')
                password = request.POST.get('password','')
                print username
                print password
                user = authenticate(username=username, password=password)
                print user
                if user is not None:
                     if user.is_active:
                        auth.login(request, user)
                        return render(request, 'Home/authhome.html',{'user':user})
                else:
                 return render(request, 'UserManagement/Papaja.html', {'error_message': 'Your account has been disabled'})
            else:
                form=UserLoginForm()
            return render(request, 'UserManagement/login.html',{'form':form})

def log_out(request):
    logout(request)
    return render_to_response('Home/index.html', {'request': request})
