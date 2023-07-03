from django.shortcuts import render, redirect
from .forms import CombinedRegistrationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import for_empresario
from .models import EmpresarioUser, EmpresarioQuestionnaire

@login_required(login_url='/empresario/')
@for_empresario
def dashboard(request):
    user = request.user
    userinfo = EmpresarioUser.objects.get(primary_email = user.email)
    if(not userinfo.questionare_submitted):
        print("didn't submit")
    context = {
        'userinfo':userinfo
    }
    return render(request, 'empresario/dashboard.html',context)

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
