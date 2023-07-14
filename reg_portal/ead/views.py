from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CombinedRegistrationForm, ProfileForm
from .decorators import for_ead
from .models import EADUser, EADNotice

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

@login_required(login_url='/ead/')
@for_ead
def dashboard(request):
    user = request.user
    userinfo = EADUser.objects.get(user__id = user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=userinfo)
        if form.is_valid():
            form.save()
            return redirect('ead_dashboard')
    else:
        form = ProfileForm(instance=userinfo)
    notices = EADNotice.objects.all().order_by('-date')

    context = {
        'userinfo':userinfo,
        'form':form,
        'notices': notices,
    }
    return render(request, 'ead/dashboard.html', context)

@login_required(login_url='/ead/')
@for_ead
def event(request):
    return render(request, 'ead/event.html')

@login_required(login_url='/ead/')
@for_ead
def result(request):
    return render(request, 'ead/result.html')

@login_required(login_url='/ead/')
@for_ead
def certificate(request):
    return render(request, 'ead/certificate.html')