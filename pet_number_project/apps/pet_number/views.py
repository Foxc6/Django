# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.db.models import Count

# Create your views here.
def welcome(request):
	pets = Pet.objects.values('name').annotate()
	context = {'pets': pets}
	return render(request, 'pet_number/welcome.html', context)

def index(request):
	pets = Pet.objects.values('name').annotate(count=(Count('name')))
	print pets
	context = {'pets': pets}
	return render(request, 'pet_number/index.html', context)

def create_pet(request):
	pet_select = Pet.objects.create(name=request.POST['name'])
	pet = Pet.objects.create(name=request.POST['name'])
	return redirect('/index')