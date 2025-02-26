from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def myfiles(request):
    return render(request, 'myfiles.html')

def mylearning(request):
    return render(request, 'mylearning.html')

def search(request):
    return render(request, 'search.html')

def nirnayai(request):
    return render(request, 'nirnayai.html')

def formfilling(request):
    return render(request, 'formfilling.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')