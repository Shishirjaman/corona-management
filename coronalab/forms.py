from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Test, RegUser


class TestForm1(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class TestForm2(ModelForm):
    class Meta:
        model = Test
        fields = ['user','testcenter','date']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class Profile(ModelForm):
    class Meta:
        model = RegUser
        fields = ['email','phone','address']