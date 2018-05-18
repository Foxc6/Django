# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
	print '/\/\/\/\/\/\/\/\/IN INDEX METHOD/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'amadon/index.html')

# Create your views here.
