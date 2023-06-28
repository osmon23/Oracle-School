from django import forms

from .models import Grade


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = (
            'name',
            'teacher',
            'student',
        )


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', )
