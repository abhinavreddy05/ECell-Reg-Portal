from django.shortcuts import render

def register(request):
    return render(request, 'ead/registration.html')

def login(request):
    return render(request, 'ead/login.html')

def dashboard(request):
    return render(request, 'ead/dashboard.html')

def event(request):
    return render(request, 'ead/dashboard.html')

def result(request):
    return render(request, 'ead/dashboard.html')

def certificate(request):
    return render(request, 'ead/dashboard.html')