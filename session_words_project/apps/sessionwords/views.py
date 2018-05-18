# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN INDEX METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'sessionwords/index.html')

def add(request):
	word_list = []
	print '/\/\/\/\/\/\/\/\/\/\/IN ADD METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	if request.method == "POST":
		request.session['word'] = request.POST['word']
		word = request.session['word']
		word_list.append(word)
		color = request.POST.get("color", None)
		print word
		print word_list
		if color in ["green"]:
			print "The green radio button was selected"
		if color in ["red"]:
			print "The red radio button was selected"
		if color in ["blue"]:
			print "The blue radio button was selected"
		largefont = request.POST.get("largefont", None)
		if 'largefont' in request.POST:
			print "The large font checkbox was selected"
		else:
			print "The large font checkbox was NOT selected"
	return redirect('show/')

def show(request):
	'/\/\/\/\/\/\/\/\/\/\/IN ADD METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'sessionwords/index.html')

def reset(request):
	print '/\/\/\/\/\/\/\/\/\/\/YOU USED THE RESET METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	request.session.clear()
	return redirect('/')

# Create your views here.
