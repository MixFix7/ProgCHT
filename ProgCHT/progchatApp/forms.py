from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)
    icon_profile = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        profile = Profile(user=user)
        if self.cleaned_data.get('icon_profile'):
            icon_profile = self.cleaned_data['icon_profile']
        profile.save()
        return user


