from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import EmpresarioUser, EmpresarioQuestionnaire
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

User = get_user_model()

class RegistrationForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ('password1',)

class EmpresarioUserForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=EmpresarioUser.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    cofounder = forms.CharField(required=False)
    cofounder_email = forms.EmailField(required=False)
    cofounder_contact = forms.CharField(required=False)
    
    class Meta:
        model = EmpresarioUser
        fields = ('company_startup_name', 'team_leader', 'team_leader_linkedin', 'gender', 'age', 'location', 'primary_email', 'primary_contact', 'cofounder', 'cofounder_email', 'cofounder_contact')

class CombinedRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registration_form = RegistrationForm(*args, **kwargs)
        self.empresario_user_form = EmpresarioUserForm(*args, **kwargs)

    def is_valid(self):
        return self.registration_form.is_valid() and self.empresario_user_form.is_valid()

    def save(self):
        user = self.registration_form.save(commit=False)
        user.username = self.empresario_user_form.cleaned_data['primary_email']
        user.name = self.empresario_user_form.cleaned_data['company_startup_name']
        user.email = self.empresario_user_form.cleaned_data['primary_email']
        user.set_password(self.registration_form.cleaned_data['password1'])
        user.empresario = True
        user.save()

        empresario_user = self.empresario_user_form.save(commit=False)
        empresario_user.user = user
        empresario_user.save()

        return user

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.empresario:
            return redirect('/empresario/register')

        # Call the parent's confirm_login_allowed method to perform other default checks
        super().confirm_login_allowed(user)
        
class EmpresarioQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = EmpresarioQuestionnaire
        exclude = ["user"]
        
        widgets = {
            'problem_solving': forms.Textarea(attrs={'rows': 3}),
            'proposed_solution': forms.Textarea(attrs={'rows': 3}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = EmpresarioUser
        fields = ('profile_image',)