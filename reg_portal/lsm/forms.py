from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import LSMUser
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

User = get_user_model()

class RegistrationForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1',)

class LSMUserForm(forms.ModelForm):
    lsm_city = forms.ChoiceField(
        choices=LSMUser.CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sector = forms.ChoiceField(
        choices=LSMUser.SECTOR,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = LSMUser
        fields = ('mobile', 'lsm_city', 'startup', 'sector')

class CombinedRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registration_form = RegistrationForm(*args, **kwargs)
        self.lsm_user_form = LSMUserForm(*args, **kwargs)

    def is_valid(self):
        return self.registration_form.is_valid() and self.lsm_user_form.is_valid()

    def cleaned_data(self):
        return {
            **self.registration_form.cleaned_data,
            **self.lsm_user_form.cleaned_data
        }

    def save(self):
        user = self.registration_form.save(commit=False)
        user.set_password(self.registration_form.cleaned_data['password1'])
        user.lsm = True
        user.save()

        lsm_user = self.lsm_user_form.save(commit=False)
        lsm_user.user = user
        lsm_user.save()

        return user

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.lsm:
            return redirect('/lsm/register')

        # Call the parent's confirm_login_allowed method to perform other default checks
        super().confirm_login_allowed(user)