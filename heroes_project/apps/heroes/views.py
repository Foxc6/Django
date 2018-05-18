# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def sessCheck(request):
	try:
		return request.session['user_id']
	except:
		return False

def welcome(request):
	return render(request, 'heroes/welcome.html')

def new_hero(request):
	context = {'powers': Power.objects.all()}
	return render(request, 'heroes/new_hero.html', context)

def create_hero(request):
	hero = Hero.objects.create(
		name=request.POST['name'],
		)
	power = Power.objects.get(id = request.POST['hero_powers'])
	hero_powers = hero.powers.add(power.id)
	context = {'powers': Power.objects.all()}
	return redirect('/hero_index', context)

def show_hero(request, id):
	hero = Hero.objects.get(id=id)
	context = {'hero': Hero.objects.get(id = id), 'powers': hero.powers.all()}
	return render(request, 'heroes/show_hero.html', context)

def new_power(request):
	return render(request, 'heroes/new_power.html')

def create_power(request):
	power = Power.objects.create(
		name=request.POST['name'],
		description=request.POST['description'],
		)
	return redirect('/hero_index')

def hero_index(request):
	context = {'heroes': Hero.objects.all()}
	return render(request, 'heroes/hero_index.html', context)

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
	return redirect('/hero_index')

def logout(request):
	request.session.flush()
	return redirect('/')
