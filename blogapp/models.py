from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class Receipe(models.Model):
    receipe_name= models.CharField( max_length=25, null=True, blank=True)
    recipe_image= models.FileField(null=True,blank=True)
    category=models.CharField( max_length= 25, null=True, blank=True )
    type=models.CharField(max_length=30, null=True, blank=True)
    step = RichTextField(null= True)
    pub_date = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    prep_time = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
            db_table="receipe"
            verbose_name_plural= "Receipe"
            ordering=['pub_date']



class Reeluser(AbstractUser):
    token=models.CharField(max_length=255, default="111", null=True)
    class Meta:
        db_table= "reeluser"
        verbose_name_plural= "Reeluser"

class Ingredients(models.Model):
    receipe_name=  models.ForeignKey(Receipe, on_delete= models.CASCADE, related_name="food", null=True, blank=True)
    ingredients= models.CharField(max_length=25, default="0")

    class Meta:
        db_table= "ingredients"
        verbose_name_plural="Ingredients"


class Comments(models.Model):
    receipe_name = models.ForeignKey(Receipe, on_delete=models.CASCADE, related_name="water", null=True, blank=True)
    name= models.CharField(max_length= 25, null=True, blank=True)
    subject= models.CharField(max_length= 25, null=True, blank=True)
    msg= models.TextField(max_length=255, null=True, blank=True)
    email= models.EmailField(max_length= 25, null= True, unique=True, blank=True)

    class Meta:
        db_table= "comments"
        verbose_name_plural="Comments"


class Slider(models.Model):
    slider_image = models.FileField(blank=True, null=True)
    slider_caption1 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption2 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "slider"
        verbose_name_plural= "Slider"



class SocialLinks(models.Model):
    icon_name = models.CharField(max_length=30, null=True, blank=True)
    social_url = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        db_table= "social_links"
        verbose_name_plural= "Social Links"

class Contact(models.Model):
    contact_name = models.CharField(max_length=25, null=True, blank=True)
    contact_subject = models.CharField(max_length=25, null=True, blank=True)
    contact_msg = models.TextField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(max_length=25, null=True, unique=True, blank=True)

    class Meta:
        db_table="contact"
        verbose_name_plural="contact"

class FooterImage(models.Model):
    image= models.FileField(null=True, blank=True)

    class Meta:
        db_table="footerimage"
        verbose_name_plural="FooterImage"









