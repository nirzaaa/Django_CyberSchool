from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile
from .models import BadProfile, Resume, Present

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # model = Profile
        model = BadProfile
        # fields = ['image']
        fields = ['image']

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']

class PresentUpdateForm(forms.ModelForm):
    class Meta:
        model = Present
        fields = ['file']
