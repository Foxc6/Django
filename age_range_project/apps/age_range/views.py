# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# Create your views here.
def sessCheck(request):
	try:
		return request.session['user_id']
	except:
		return False
		
def index(request):
	return render(request, 'age_range/index.html')

def under_10(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	user_age = request.session['user_age']
	if user_age > 10:
		print "hello"

	return render(request, 'age_range/under_10.html', context)

def eleven_18(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/eleven_18.html', context)

def nineteen_24(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/nineteen_24.html', context)

def twentyfive_35(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/twentyfive_35.html', context)

def thirtysix_50(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/thirtysix_50.html', context)

def over_51(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/over_51.html', context)

def UserCount(request):
	users = {'users': User.objects.all()}
	under_10_count = 0
	eleven_18_count = 0
	nineteen_24_count = 0
	twentyfive_35_count = 0
	thirtysix_50_count = 0
	over_51_count = 0

	for user in users:
		if user.age < 10:
			under_10_count += 1
		if user.age >= 10 and user.age < 19:
			eleven_18_count +=1
		if user.age >= 19 and  user.age< 25:
			nineteen_24_count +=1
		if user.age >= 25 and  user.age< 36:
			twentyfive_35_count +=1
		if user.age >= 36 and  user.age< 51:
			thirtysix_50_count +=1
		if user.age >= 51:
			over_51_count +=1
	return redirect('age_range/home.html')




def register(request):
	results =  User.objects.RegVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	user = User.objects.UserCreator(request.POST)
	messages.success(request, 'User has been created. Please login to continue!')
	return redirect('/')

def login(request):
	results = User.objects.LogVal(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = results['user'].id
	request.session['user_name'] = results['user'].name
	request.session['user_age'] = results['user'].age
	return redirect('/home')

def home(request):
	if sessCheck(request) == False:
		return redirect('/')
	context = {'users': User.objects.all()}
	return render(request, 'age_range/home.html', context)

def delete(request, id):
	user = User.objects.get(id = id)
	user.delete()
	return render(request, 'age_range/home.html', {'users': User.objects.all()})

def logout(request):
	request.session.flush()
	return redirect('/')


