from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Employee


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2',)


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, help_text='Required..')
    last_name = forms.CharField(max_length=100, required=False, help_text='Required...')
    email = forms.EmailField(max_length=100, help_text='Required. Need a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    gender = forms.CharField(max_length=10, required=True, help_text='Required..')
    date_of_birth = forms.DateField(required=True, help_text='Required..')
    designation = forms.CharField(max_length=100, required=True, help_text='Required..')
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'birth_date', 'gender', 'designation', 'date_of_birth')
