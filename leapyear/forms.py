# leapyear/forms.py
from django import forms

class YearForm(forms.Form):
    year = forms.IntegerField(label='Enter Year', min_value=0)
