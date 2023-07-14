from django.shortcuts import render, redirect
from .forms import CombinedRegistrationForm, CustomAuthenticationForm, EmpresarioQuestionnaireForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .decorators import for_empresario
from .models import EmpresarioUser, EmpresarioQuestionnaire, EmpresarioNotice

@login_required(login_url='/empresario/')
@for_empresario
def dashboard(request):
    user = request.user
    userinfo = EmpresarioUser.objects.get(user__id = user.id)
    if(not userinfo.questionare_submitted):
        questionnaire = True
        if request.method == "POST":
            form = EmpresarioQuestionnaireForm(request.POST)
            if form.is_valid():
                questionnairedata = form.save(commit=False)
                questionnairedata.user = request.user  # Assuming you have a user associated with the questionnaire
                questionnairedata.save()
                
                userinfo.questionare_submitted = True
                userinfo.save()
                return redirect('empresario_dashboard')
        else:
            form = EmpresarioQuestionnaireForm()
    else:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=userinfo)
            if form.is_valid():
                form.save()
                return redirect('empresario_dashboard')
        else:
            form = ProfileForm(instance=userinfo)
        questionnaire = False
    notices = EmpresarioNotice.objects.all().order_by('-date')

    context = {
        'userinfo':userinfo,
        'questionnaire':questionnaire,
        'form':form,
        'notices': notices
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
