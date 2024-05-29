from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Posts

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','profile_picture']

class CreatePost(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','description']