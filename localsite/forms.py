from django.forms import ModelForm
from .models import Uang
from django.forms import PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UangForm(ModelForm):
	class Meta:
		model = Uang
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']