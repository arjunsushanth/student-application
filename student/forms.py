from django import forms
from student.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class StudentLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))