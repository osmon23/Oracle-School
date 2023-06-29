from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django_flatpickr.widgets import DatePickerInput

from .models import Teacher, Student

User = get_user_model()


class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = (
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'grade',
            'subject',
        )


class TeacherLoginForm(forms.Form):
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=13,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'full_name',
            'email',
            'date_of_birth',
            'grade',
            'address',
            'gender',
            'photo',
        )
        widgets = {
            'date_of_birth': DatePickerInput(),
        }


class NewsletterForm(forms.Form):
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea)
