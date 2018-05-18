# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN INDEX METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'user_login/index.html')
# Create your views here.