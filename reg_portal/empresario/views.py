from django.shortcuts import render, redirect
from .forms import CombinedRegistrationForm, CustomAuthenticationForm

def login(request):
    return render(request, 'empresario/login.html')

def register(request):
    if request.method == 'POST':
        form = CombinedRegistrationForm(request.POST)
        if form.is_valid():
            # Save User object
            user = form.save()

            # Save additional data
            empresario_user = form.save()
            empresario_user.user = user
            empresario_user.save()

            return redirect('/empresario/login/')
    else:
        form = CombinedRegistrationForm()

    context = {'form': form}

    return render(request, 'empresario/registration.html', context)
