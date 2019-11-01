from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView,View
from django.http import HttpResponse,request
from django.views.generic.detail import DetailView
from . models import Receipe,Ingredients,Comments,Reeluser,Slider,SocialLinks,Contact
from . forms import Signup,Loginform
import json
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import datetime
from django.core.mail import send_mail
from django.db.models import Q




class Home(View):

    def get(self,request):
        form=Signup()
        form1 = Loginform()
        query1 = Receipe.objects.all().order_by('-pub_date')[:6]
        query2= Slider.objects.all()
        query3 = SocialLinks.objects.all()
        print(query3)
        return render(request,"index.html",{'myobj':form, 'mylogin':form1, 'query1':query1, "slide" : query2, 'social_icons':query3})

    def linkmail(request):
        token=request.GET["token"]
        mail=request.GET["email"]
        ob= Reeluser.objects.get(email=mail)
        if ob.token==token:
            ob.is_active=True
            ob.save()
            return redirect("/")
        else:
            return HttpResponse("invalid token")

    def post(self,request):
        dict1={}
        form=Signup(request.POST)
        if form.is_valid() :
            name=form.cleaned_data['name']
            username = form.cleaned_data['username']
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            con_password=form.cleaned_data['conpass']

            try:
                if (password==con_password):
                    timestamp=datetime.datetime.timestamp(datetime.datetime.now())
                    u1=Reeluser(first_name=name,username=username,email=mail,password=password, is_superuser=0)
                    u1.set_password(password)
                    token= account_activation_token._make_hash_value(u1,timestamp)
                    u1.token=token
                    msg="http://127.0.0.1:8000/email/?token="+token+"email="+mail
                    send_mail("please confirm your email", msg, 'jaimoljoseph.cst@gmail.com', [mail], fail_silently=False)
                    u1.save()
                    dict1["status"]=1

                else:
                    print("inside else case of try pg")
                    dict1["status"]=0
            except Exception as e:
                print("exception in home function",e)
        else:
            print("inside not valid else case of hom pg")
            dict1["errors"]=1
            dict1["key"]=form.errors
        jsondata=json.dumps(dict1)
        return HttpResponse(jsondata, content_type="application/json")


class Login(View):

    def post(self,request):
        dict2={}
        form1=Loginform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['name']
            password = form1.cleaned_data['password']
            try:
                u2=Reeluser.objects.get(username=username)
                user=u2.username
                check_pass=u2.password
                auth1=authenticate(request, username=username, password=password)
                if(auth1 is not None):
                    login(request, auth1, backend= 'django.contrib.auth.backends.ModelBackend')
                    dict2["val1"]=1
                else:
                    dict2["val1"]=0
            except Exception as e:
                dict2["val1"]=2
                print("exception in login function",e)
        else:
            dict2["val1"]=5

        jsondata=json.dumps(dict2)
        return HttpResponse(jsondata, content_type="application/json")

    def logout_view(request):
        logout(request)
        form = Signup()
        form1 = Loginform()
        query1 = Receipe.objects.all().order_by('-pub_date')[:6]
        query2 = Slider.objects.all()
        return render(request, "index.html", {'myobj': form, 'mylogin': form1, 'query1': query1, "slide": query2})



class Listitems(View):

    def get(self, request):

        queryset = Receipe.objects.all()
        query3 = SocialLinks.objects.all()
        return render(request, "recipes.html", {'recipes':queryset,'social_icons':query3})

    def post(self, request):
        type= request.POST['type']
        name = request.POST['name']
        category = request.POST['category']

        query_recipe = Receipe.objects.filter(Q(category__contains=category)).filter(Q(type__contains=type)).filter(Q(receipe_name__contains=name))
        print("query------------------------------", query_recipe)
        return render(request,"recipes.html", {"recipes":query_recipe})




class Details(DetailView):
    model = Receipe
    queryset = Receipe.objects.all()
    template_name = "recipe-single.html"
    context_object_name = "view"


class Comment(View):

    def get(self, request):
        query3 = SocialLinks.objects.all()
        return render(request, "single-recipe.html", {'icon' : query3})

    def post(self, request):
            dict6 = {}
            name=request.user
            receipe_name=request.POST['name']
            email=request.POST['email']
            subject= request.POST['subject']
            message= request.POST['message']
            if (name != "" and email != "" and subject != "" and message != ""):
                r1= Receipe.objects.get(receipe_name=receipe_name)
                c1= Comments(name=name,subject=subject, email=email, msg=message, receipe_name=r1)
                c1.save()
                dict6["status"]=1
            else:
                dict6["status"]=0
            print("dict6-------------->>>", dict6)
            jsondata=json.dumps(dict6)
            return HttpResponse(jsondata, content_type="application/json")



class About(View):

    def get(self, request):
        return render(request, "about.html")

class Contact(View):

    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        dict7={}
        name= request.POST['name']
        email= request.POST['email']
        subject=request.POST['subject']
        message= request.POST['message']
        if(name!="" and email!="" and subject!="" and message!=""):
            c4= Contact(name=name, email=email, subject=subject, message= message )
            c4.save()
            dict7["status"]="success"
        else:
            dict7["status"]= "failed"

        jsondata= json.dumps(dict7)
        return HttpResponse(jsondata, content_type="application/json")























