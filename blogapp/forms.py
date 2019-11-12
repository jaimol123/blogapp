from django import forms
from . models import Reeluser,Receipe, Newsletter,Comments,Contact
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
    name = forms.CharField(label="NAME",widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=255)
    password = forms.CharField(label="PASSWORD:", widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True,max_length=255)



    class Meta:
        model = Reeluser;

class Newsletters(forms.Form):
    email = forms.EmailField(label="email", widget=forms.TextInput(attrs={'class': "newsletter-form"}), required=True,max_length=255)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Newsletter.objects.filter(mail=email):
            raise forms.ValidationError("email already exist !!!!")
        if( '@' not in email):
            raise forms.ValidationError("enter a valid email id !!!!")
        return email

    class Meta:
        model = Newsletter;


class Reviews(forms.Form):

    subject = forms.CharField(label = '', widget=forms.TextInput(attrs={'class':"comment-form",'placeholder':'Subject'}), required = True, max_length=255)
    message = forms.CharField(label = '', widget=forms.Textarea(attrs={'class':"comment-form",'placeholder':'Message'}), required = True, max_length=255)

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        for i in subject:
            if (i.isdigit()):
                raise forms.ValidationError('numeric values not allowed')
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message')
        for i in message:
            if (i.isdigit()):
                raise forms.ValidationError('numeric values not allowed')
        return message

    class Meta:
        model = Comments

class Contactform(forms.Form):
    print("inside forms.py")
    name =  forms.CharField(label ='',widget=forms.TextInput(attrs={'class':"contact-form" , 'placeholder':'Name'}), required = True, max_length=255)
    email =  forms.CharField(label = '', widget=forms.TextInput(attrs={'class':"contact-form",'placeholder':'Email'}), required = True, max_length=255)
    subject = forms.CharField(label = '', widget=forms.TextInput(attrs={'class':"contact-form",'placeholder':'Subject'}), required = True, max_length=255)
    message =  forms.CharField(label = '', widget=forms.Textarea(attrs={'class':"contact-form",'placeholder':'Message'}), required = True, max_length=255)

    def clean_email(self):
        print("inside email")
        email = self.cleaned_data['email']
        if('@' not in email):
            raise forms.ValidationError('enter a valid email id')
        return email

    def clean_subject(self):
        print("inside subject")
        subject = self.cleaned_data['subject']
        for i in subject:
            if(i.isdigit()):
                raise forms.ValidationError('numeric values not allowed')
        return subject

    def clean_message(self):
        print("inside msg")
        message = self.cleaned_data['message']
        for i in message:
            if (i.isdigit()):
                raise forms.ValidationError('numeric values not allowed')
        return message


    class Meta:
        model = Contact;





