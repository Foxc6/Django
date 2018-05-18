# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	print '/\/\/\/\/\/\/\/\/\/\/IN INDEX METHOD\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
	return render(request, 'book_authors/index.html')