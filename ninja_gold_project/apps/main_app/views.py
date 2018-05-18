# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
	try: 
		request.session['gold']
	except: 
		request.session['gold'] = 0

	try: 
		request.session['activities']
	except: 
		request.session['activities'] = []

	return render(request, 'main_app/index.html')

def process(request):
	if request.POST['building'] == 'house':
		request.session['gold'] += 9999

	if request.POST['building'] == 'farm':
		request.session['gold'] += 9999

	if request.POST['building'] == 'school':
		request.session['gold'] += 9999
		for i in range(0, len(request.session['activities'])):
			request.session['activities'][i] = 'hodor'

	print request.session['activities'], '****************************'
	return redirect('/')
