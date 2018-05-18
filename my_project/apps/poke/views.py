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
	return render(request, 'poke/welcome.html')

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
	request.session['user_name'] = results['user'].name
	return redirect('/index')

def add_poke(request, id):
	user = User.objects.get(id = id)
	logged_user = User.objects.get(id = request.session['user_id'])
	logged_user.poked_users.add(user.id)
	return redirect('/index')

def index(request):
	if sessCheck(request) == False:
		return redirect('/')
	user = User.objects.get(id = request.session['user_id'])
	other_users = User.objects.exclude(id = request.session['user_id'])
	user_poked_by = []
	for user in other_users:
		if user.poked_users.filter(id = request.session['user_id']).exists():
			user_poked_by.append(user.name)
	poked_count = len(user_poked_by)
	users = User.objects.all()
	context = {'users': users, 'poked_users': user.poked_users.all(), 'user_poked_by': user_poked_by, 'poked_count': poked_count}
	return render(request, 'poke/index.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')
