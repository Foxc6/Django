# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def sessionCheck(request):
	try:
		return request.session['user_id']
	except:
		return False

def welcome(request):
	return render(request, 'friends/welcome.html')

def add_friend(request, id):
	logged_user = User.objects.get(id = request.session['user_id'])
	new_friend = User.objects.get(id = id)
	logged_user.friends.add(new_friend.id)
	return redirect('/index')

def remove_friend(request, id):
	logged_user = User.objects.get(id = request.session['user_id'])
	remove_friend = User.objects.get(id = id)
	logged_user.friends.remove(remove_friend.id)
	return redirect('/index')

def show_user(request, id):
	user = User.objects.get(id=id)
	context = {'user': user}
	return render(request, 'friends/show_user.html', context)

def index(request):
	if sessionCheck(request) == False:
		return redirect('/')
	logged_user = User.objects.get(id = request.session['user_id'])
	friends = logged_user.friends.all()
	non_friends = User.objects.all().exclude(id__in=friends).exclude(id = logged_user.id)
	context = {'friends': friends, 'non_friends': non_friends}
	return render(request, 'friends/index.html', context)

def register(request):
	results =  User.objects.RegistrationValidator(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	user = User.objects.UserCreator(request.POST)
	messages.success(request, 'User has been created. Please log into continue!')
	return redirect('/')

def login(request):
	results = User.objects.LoginValidator(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = results['user'].id
	request.session['user_name'] = results['user'].name
	return redirect('/index')

def logout(request):
	request.session.flush()
	return redirect('/')
