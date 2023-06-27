from django.shortcuts import render, redirect
from .forms import CombinedRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CombinedRegistrationForm(request.POST)
        if form.is_valid():
            # Save User object
            user = form.save()

            # Save additional data
            ead_user = form.save()
            ead_user.user = user
            ead_user.save()

            return redirect('/ead/login/')
    else:
        form = CombinedRegistrationForm()

    context = {'form': form}

    return render(request, 'ead/registration.html', context)


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