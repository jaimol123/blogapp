from django import forms
from . models import Reeluser,Receipe
from django.core.exceptions import ValidationError

class Signup(forms.Form):

    name= forms.CharField(label=' NAME:',widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100)
    username = forms.CharField(label='ENTER YOUR USERNAME:', widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100, required=True)
    mail = forms.CharField(label='ENTER YOUR EMAIL ID:', widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:400px'}),max_length=100, required=True)
    password= forms.CharField(label='PASSWORD',widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width:400px'}), required=True)
    conpass= forms.CharField(label='CONFIRM PASSWORD',widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'width:400px'}), required=True)

    def clean_password(self):

        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

    def clean_username(self):

         username= self.cleaned_data.get('username')
         if Reeluser.objects.filter(username=username) :
             raise forms.ValidationError("username already exist !!!!")
         return username

    def clean_mail(self):

         mail= self.cleaned_data.get('mail')
         if Reeluser.objects.filter(email=mail) :
            raise forms.ValidationError("email already exist !!!!")
         return mail

    def clean_name(self):
        name= self.cleaned_data.get('name')
        for i in name:
            if(i.isdigit()):
                raise forms.ValidationError("numeric values not allowed")
            return name


    class Meta:
        model = Reeluser;


class Loginform(forms.Form):
    name = forms.CharField(label="NAME",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="PASSWORD:", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)


    class Meta:
        model = Reeluser;





