from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
def index(request):
    return render(request, 'surveys/index.html')
def process_form(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    request.session['name'] = request.POST.get('name', False)
    request.session['location'] = request.POST.get('location', False)
    request.session['language'] = request.POST.get('language', False)
    request.session['comments'] = request.POST.get('comments', False)
    return redirect('/surveys/result')
def result(request):
    counter = request.session['counter']
    name = request.session['name']
    location = request.session['location']
    language = request.session['language']
    comments = request.session['comments']
    counter = request.session['counter']
    context = {
        'name': name,
        'location': location,
        'language': language,
        'comments': comments,
        'counter' : counter,
    }
    return render(request, 'surveys/result.html', context)
