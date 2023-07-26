from django import forms

class CreateNewPost(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    text = forms.CharField(label="Text", max_length=500000)
    # check = forms.BooleanField(required=False)

class Calculation(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    text = forms.CharField(label="Calculation", max_length=500000)

class Ssti(forms.Form):
    text = forms.CharField(max_length=500000)
