
from django import forms

class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()