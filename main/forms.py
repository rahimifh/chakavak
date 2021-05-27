from django import forms
from .models import apply,pish
class Apply_form(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['full_name', 'email', 'phone', 'address','text']
class Apply_formm(forms.ModelForm):
    class Meta:
        model = pish
        fields = ['full_name', 'email','text']
