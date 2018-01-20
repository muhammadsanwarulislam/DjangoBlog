from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = articale
        fields = [
        'title',
        'articale_body',
        'image',
        'category',
        ]
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields =[
              'first_name',
              'last_name',
              'email',
              'username',
              'password1',
              'password2',
        ]

class CreateAuthor(forms.ModelForm):
    class Meta:
        model=author
        fields=[
            'author_image',
            'details',
        ]