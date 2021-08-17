from django import forms
from django.db.models.fields import EmailField

class cartForm(forms.Form):
    quantity = forms.IntegerField(max_value=20, min_value=1)


class checkoutForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=30, required=True)
    