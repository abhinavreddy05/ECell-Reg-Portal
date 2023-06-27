from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from ead.models import EADUser

User = get_user_model()

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EADUserForm(forms.ModelForm):
    ead_city = forms.ChoiceField(
        choices=EADUser.CITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = EADUser
        fields = ('mobile', 'college_name', 'ead_city')

class CombinedRegistrationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registration_form = RegistrationForm(*args, **kwargs)
        self.ead_user_form = EADUserForm(*args, **kwargs)

    def is_valid(self):
        return self.registration_form.is_valid() and self.ead_user_form.is_valid()

    def save(self):
        user = self.registration_form.save(commit=False)
        user.set_password(self.registration_form.cleaned_data['password1'])
        user.ead = True
        user.save()

        ead_user = self.ead_user_form.save(commit=False)
        ead_user.user = user
        ead_user.save()

        return user
