from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    money = forms.FloatField(label='money')
    day = forms.DateField(label='day')
