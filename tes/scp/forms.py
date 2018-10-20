from django import forms


class AddForm(forms.Form):
    key = forms.CharField(max_length=6000)
