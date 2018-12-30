from django import forms
from django.contrib.admin import widgets as adminwidget
from .models import Visualization, Income_visualization



class MoneyForm(forms.ModelForm):
    class Meta:
        model = Visualization
        fields = ['name', 'money', 'day']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income_visualization
        fields = ['name','income']