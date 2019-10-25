from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


class Receipe(models.Model):
    receipe_name= models.CharField(max_length=25)
    category=models.CharField(max_length= 25 )
    type=models.CharField(max_length=30)
    step = models.CharField(max_length=25)
    pub_date = models.DateField(datetime.datetime.now)
    prep_time = models.CharField(max_length=25)

    class Meta:
        db_table= "receipe"

class Reeluser(AbstractUser):

    class Meta:
        db_table= "reeluser"

class Ingredients(models.Model):
    receipe_name=  models.ForeignKey(Receipe, on_delete= models.CASCADE, related_name="food")
    ingredients= models.CharField(max_length=25, default="0")

    class Meta:
        db_table= "ingredients"


class Comments(models.Model):
    receipe_name = models.ForeignKey(Receipe, on_delete=models.CASCADE, related_name="water")
    name= models.CharField(max_length= 25)
    subject= models.CharField(max_length= 25)
    msg= models.TextField()
    email= models.EmailField(max_length= 25, null= True, unique=True)

    class Meta:
        db_table= "comments"







