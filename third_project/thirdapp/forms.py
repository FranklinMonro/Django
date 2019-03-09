from django import forms

class Formsname(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    text = forms.CharField( widget = forms.Textarea)
