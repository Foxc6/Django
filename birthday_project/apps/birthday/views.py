# -*- coding: utf-8 -*-
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def sessCheck(request):
	try:
		return request.session['user_id']
	except:
		return False

#Create your views here

def welcome(request):
	return render(request, 'birthday/welcome.html')

def register(request):
	results =  User.objects.RegVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	user = User.objects.creator(request.POST)
	messages.success(request, 'User has been created. Please log into continue!')
	return redirect('/')

def login(request):
	results = User.objects.LogVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = results['user'].id
	request.session['user_first_name'] = results['user'].first_name
	return redirect('/index')

def index(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'birthday/index.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')

