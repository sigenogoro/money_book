from django import forms
from django.contrib.admin import widgets as adminwidget
from .models import Visualization



class MoneyForm(forms.ModelForm):
    class Meta:
        model = Visualization
        fields = ['name', 'money', 'day']
