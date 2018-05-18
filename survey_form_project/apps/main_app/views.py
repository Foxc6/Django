# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN INDEX METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'main_app/index.html')

def create(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN CREATE METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1
	if request.method == "POST":
		request.session['username'] = request.POST['username']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	return redirect('show/')

def show(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN SHOW METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'main_app/show.html')

def reset(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
