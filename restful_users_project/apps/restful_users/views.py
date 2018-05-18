# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from models import *

def index(request):
	return render(request, 'restful_users/index.html', {'users': User.objects.all()})

def new(request):
	return render(request, 'restful_users/new.html')

def create(request):
	user = User.objects.create(
		first_name=request.POST['first_name'], 
		last_name=request.POST['last_name'], 
		email=request.POST['email']
		)
	return redirect('/')

def edit(request, id):
	context = {}
	return render(request, 'restful_users/edit.html', {'user': User.objects.get(id = id)})

def show(request, id):
	return render(request, 'restful_users/show.html', {'user': User.objects.get(id = id)})

def delete(request, id):
	user = User.objects.get(id = id)
	user.delete()
	return render(request, 'restful_users/index.html', {'users': User.objects.all()})

def update(request, id):
	user = User.objects.get(id = id)
	user.first_name=request.POST['first_name']
	user.last_name=request.POST['last_name']
	user.email=request.POST['email']
	user.save()
	return redirect('/')