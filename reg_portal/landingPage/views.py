from django.shortcuts import render

def home(request):
    return render(request, 'landingPage/landing.html')

def about(request):
    return render(request, 'landingPage/about.html')

def contact(request):
    return render(request, 'landingPage/contact.html')