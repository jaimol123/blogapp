from django import forms
from . models import Reeluser
from django.core.exceptions import ValidationError


class Signup(forms.Form):
    name= forms.CharField(label='ENTER YOUR NAME:',max_length=100,required=True)
    username = forms.CharField(label='ENTER YOUR USERNAME:', max_length=100, required=True)
    mail = forms.EmailField(label='ENTER YOUR EMAIL ID:', max_length=100, required=True)
    password= forms.CharField(widget=forms.PasswordInput)
    conpass= forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password


    class Meta:
        model = Reeluser;


class Loginform(forms.Form):
    name=forms.CharField(label="USERNAME:", max_length=100, required=True)
    password=forms.CharField(label="PASSWORD:",widget=forms.PasswordInput, required=True)

    class Meta:
        model = Reeluser;










# class Receipenames(forms.Form):
#     receipe_name = forms.CharField(label='rname', max_length=100)
#     typename= forms.CharField(label='cname', max_length=100)
#     daytype= forms.CharField(label='tname', max_length=100)
#     stepname=forms.CharField(label='sname', max_length=100)
#     published=forms.DateField(label='pdate')
#     preptime= forms.TimeField(label='ttime')