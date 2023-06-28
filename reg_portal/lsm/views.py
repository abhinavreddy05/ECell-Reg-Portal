from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CombinedRegistrationForm
from .decorators import for_lsm

def register(request):
    if request.method == 'POST':
        form = CombinedRegistrationForm(request.POST)
        if form.is_valid():
            # Save User object
            user = form.save()

            # Save additional data
            lsm_user = form.save()
            lsm_user.user = user
            lsm_user.save()

            return redirect('/lsm/login/')
    else:
        form = CombinedRegistrationForm()

    context = {'form': form}

    return render(request, 'lsm/registration.html', context)

@login_required(login_url='/ead/')
@for_lsm
def dashboard(request):
    return render(request, 'lsm/dashboard.html')