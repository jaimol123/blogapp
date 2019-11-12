from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView,View
from django.http import HttpResponse,request
from django.views.generic.detail import DetailView
from . models import Receipe,Ingredients,Comments,Reeluser,Slider,SocialLinks,Contact,FooterImage,Feature, AboutUs, Rating, Newsletter,Address
from . forms import Signup,Loginform, Newsletters,Reviews,Contactform
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
import smtplib




class Home(View):

    def get(self,request):
        form=Signup()
        form1 = Loginform()
        query1 = Receipe.objects.all().order_by('-pub_date')[:6]
        query2= Slider.objects.all()
        query3 = SocialLinks.objects.all()
        query4= FooterImage.objects.all()
        query5 = Rating.objects.order_by('avg')[:4]

        return render(request,"index.html",{'myobj':form, 'mylogin':form1, 'query1':query1, "slider" : query2, 'social_icons':query3, 'footerimg':query4 , 'rate': query5})

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
                    #send_mail("please confirm your email", msg, 'jaimoljoseph.cst@gmail.com', [mail], fail_silently=False)
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
            dict2["val1"] = 3


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
        form = Signup()
        form1 = Loginform()
        queryset = Receipe.objects.order_by('-id')
        paginator = Paginator(queryset, 6)
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        categories = Receipe.objects.all().values_list('category', flat=True)
        query3 = SocialLinks.objects.all()
        query4 = FooterImage.objects.all()
        query5 = Rating.objects.all()

        return render(request, "recipes.html", {'myobj':form, 'mylogin':form1,'recipes':recipes,'social_icons':query3, 'footerimg': query4, 'categories':categories, 'rate' : query5})

    def post(self, request):
        dict10={}
        categories = Receipe.objects.all().values_list('category', flat=True)
        type= request.POST['type']
        name = request.POST['name']
        category = request.POST['category']
        print("-----------------",type,category,name)
        r1 = Receipe.objects.all()
        query_recipe = Receipe.objects.filter(Q(category__contains=category)).filter(Q(type__contains=type)).filter(Q(receipe_name__contains=name))
        print("query of receipe --====------------------------------", query_recipe)

        return render(request,"recipes.html", {"recipes":query_recipe, 'categories':categories})




class Details(DetailView):
    model = Receipe
    queryset= Receipe.objects.all()
    form = Signup()
    form1 = Loginform()
    template_name = "recipe-single.html"
    context_object_name = "view"


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['category'] = Receipe.objects.all().values_list('category', flat=True)
        data['comments'] = Comments.objects.all()[:5]
        data['count'] = Comments.objects.all().count()
        data['myobj'] = Signup()
        data['mylogin'] = Loginform()
        print("inside get fn")
        data['reviews'] = Reviews()

        return data





class Comment(View):

    def post(self, request):
            print("inside post fn")
            dict6 = {}
            name = request.user
            r1 = Reeluser.objects.get(first_name = name )
            email = r1.email
            idno = request.POST['idno']
            rate = request.POST['rate']

            reviews = Reviews(request.POST)

            if(reviews.is_valid()):
                print("inside isvalid")
                subject = reviews.cleaned_data['subject']
                message = reviews.cleaned_data['message']



                c1 = Comments(name=name, subject=subject, email=email, msg=message, receipe_name_id=idno,rating=rate)
                c1.save()
                dict6["status"] = 1



                dict6['name']=name
                dict6['msg']=message

                calc = Comments.objects.filter(receipe_name__id=int(idno))
                count = Comments.objects.filter(receipe_name__id=int(idno)).count()
                recipe = Receipe.objects.get(id=int(idno))
                rimage = recipe.recipe_image
                rname = recipe.receipe_name
                print(rname, calc, count)
                if (count == 1):
                    print("inside 1")
                    rate = Rating(receipe_name=rname, total=rate, avg=rate, image=rimage)
                    rate.save()

                elif (count > 1):
                    print("inside 2")
                    r1 = Rating.objects.get(receipe_name=rname)
                    total = r1.total
                    total = total + int(rate)
                    average = total / count
                    r1.total = total
                    r1.avg = average
                    r1.save()
                else:
                    pass;
                    jsondata = json.dumps(dict6)
                    return HttpResponse(jsondata, content_type="application/json")




            else:
                print(reviews.errors)
                dict6["status"] = reviews.errors
            jsondata = json.dumps(dict6)
            return HttpResponse(jsondata, content_type="application/json")






class About(View):

    def get(self, request):
        new = Newsletters()
        form = Signup()
        form1 = Loginform()
        link = SocialLinks.objects.all()
        query4 = FooterImage.objects.all()
        query5= Feature.objects.all()
        query6= AboutUs.objects.all()
        return render(request, "about.html",{'myobj': form, 'mylogin': form1,'links': link, 'footerimg': query4, 'feature':query5, 'aboutus': query6, 'newsletter' : new })

    def post(self, request):
        dict15 = {}
        new = Newsletters(request.POST)
        if new.is_valid() :
            mail = new.cleaned_data['email']
            print("mail---", mail)
            n1 = Newsletter(mail=mail)
            n1.save()
            dict15['status'] = 1
        else:
            dict15['status'] = new.errors
        jsondata = json.dumps(dict15)
        return HttpResponse(jsondata , content_type="application/json")

class ContactView(View):

    def get(self, request):
        form = Signup()
        form1 = Loginform()
        contactform = Contactform()
        link = SocialLinks.objects.all()
        query4 = FooterImage.objects.all()
        query5 = Address.objects.all()
        return render(request, "contact.html", {'myobj': form, 'mylogin': form1,'links': link, 'footerimg':query4, 'contactform':Contactform, 'query5':query5 })

    def post(self, request):
        dict7={}
        contactform = Contactform(request.POST)
        if(contactform.is_valid()):

                name = contactform.cleaned_data['name']
                email = contactform.cleaned_data['email']
                subject = contactform.cleaned_data['subject']
                message = contactform.cleaned_data['message']

                contact = Contact()

                contact.contact_msg = message
                contact.contact_email = email
                contact.contact_name = name
                contact.contact_subject = subject
                contact.save()
                send_mail(subject, message, email, ['jaimoljoseph123456@gmail.com'],fail_silently=False )
                dict7["status"]=2
        else:
                print(contactform.errors)
                dict7["status"]= contactform.errors

        jsondata= json.dumps(dict7)
        return HttpResponse(jsondata, content_type="application/json")























