from django.shortcuts import render
from django.views.generic import ListView,TemplateView,View
from django.http import HttpResponse,request
from django.views.generic.detail import DetailView
from . models import Receipe,Ingredients,Comments,Reeluser
from . forms import Signup,Loginform
import json
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email


class Home(View):


    def get(self,request):
        form=Signup()
        form1 = Loginform()
        return render(request,"index.html",{'myobj':form, 'mylogin':form1})

    def post(self,request):
        dict1={}
        form=Signup(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            username = form.cleaned_data['username']
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            con_password=form.cleaned_data['conpass']



            try:
                if(password==con_password):
                    u1=Reeluser(first_name=name,username=username,email=mail,password=password)
                    u1.set_password(password)
                    u1.save()
                    dict1["status"]=1
                else:
                    dict1["status"]=0
            except Exception as e:
                print("exception in home function",e)
        else:
            #print("form errrr",form.errors)
            dict1["errors"]=1
            dict1["key"]=form.errors

            print("non field-----------", form.non_field_errors())

        jsondata=json.dumps(dict1)

        return HttpResponse(jsondata, content_type="application/json")


class Login(View):
    @login_required
    def post(self,request):
        dict2={}
        form1=Loginform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['name']
            password = form1.cleaned_data['password']
            print("user pass----------->>>>",password)
            try:
                u2=Reeluser.objects.get(username=username)
                user=u2.username
                check_pass=u2.password
                print("------------->>>password",check_pass)
                check=check_password(password,u2.password)
                print("===================>>>>>",check)
                if(user==username and check):
                    dict2["val1"]=1
                else:
                    dict2["val1"]=0
            except Exception as e:
                dict2["val1"]=2
                print("exception in login function",e)

        jsondata=json.dumps(dict2)
        return HttpResponse(jsondata, content_type="application/json")











