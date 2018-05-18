from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'randomword/index.html')

def randomword(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for times in range (0, 14):
        word = word + str(random.choice(characters))
    words = {
        'random_word': word
    }
    return render(request, 'randomword/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
