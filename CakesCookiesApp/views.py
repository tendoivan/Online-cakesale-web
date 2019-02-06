# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def index (request):
	return render(request,'Home.html')


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return render(request, 'Home.html')
	else:
		form = AuthenticationForm()
	return render(request,'login.html', {'form':form})