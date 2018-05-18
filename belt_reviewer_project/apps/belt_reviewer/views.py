# -*- coding: utf-8 -*-
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def sessCheck(request):
	try:
		return request.session['user_id']
	except:
		return False

def welcome(request):
	return render(request, 'belt_reviewer/welcome.html')

def register(request):
	results =  User.objects.RegVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	user = User.objects.UserCreator(request.POST)
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
	return redirect('/books')

def books(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'belt_reviewer/books.html', context)

def delete(request, id):
	user = User.objects.get(id = id)
	user.delete()
	return redirect('/books')

def logout(request):
	request.session.flush()
	return redirect('/')