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

class Sqli(forms.Form):
    query = forms.CharField(label='Enter author name:', max_length=500000)

class Ssrf(forms.Form):
    url = forms.CharField(label='Try to access http://localhost:8000/thisissecret', max_length=500000)
