from django import forms


class CalculateForm(forms.Form):
    number1 = forms.NumberInput()
    number2 = forms.NumberInput()
