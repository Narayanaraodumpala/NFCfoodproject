from django.db import models
from s_adminapp.models import *


# Create your models here.
class RestarentModel(models.Model):
      Restaurant_Id=models.AutoField(primary_key=True)
      Restaurant_Name=models.CharField(unique=True,max_length=40)
      Restaurant_Email=models.EmailField(unique=True)
      Restaurant_Contact_No=models.IntegerField(unique=True)
      Restaurant_Password=models.IntegerField()
      Restaurant_Otp=models.IntegerField()
      Restaurant_Status=models.CharField(max_length=20)
      Restaurant_Area=models.ForeignKey(AreaModel,on_delete=models.CASCADE)
      Restaurant_Type=models.ForeignKey(Type_of_resModel,on_delete=models.CASCADE)

class Type_of_foodmodel(models.Model):
      Food_Id=models.IntegerField(primary_key=True)
      Food_Type=models.CharField(unique=True,max_length=30)

      def __str__(self):
            return self.Food_Type

class Food_model(models.Model):
      Food_id=models.IntegerField(default=None,null=True)
      Food_Name=models.CharField(max_length=50,primary_key=True)
      Food_price=models.CharField(max_length=10,default=None,null=True,blank=True)
      Food_Description = models.CharField(max_length=1000, default=None, null=True, blank=True)
      Food_Image=models.ImageField(upload_to='foods/',unique=True)
      Food_Type=models.ForeignKey(Type_of_foodmodel,on_delete=models.CASCADE)

class ProfileModel(models.Model):
      profile=models.CharField(max_length=2,primary_key=True,default=None)
      Profile_Image=models.ImageField(upload_to='profiles/')

class UserProfileSessionModel(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=7)
    Phone=models.IntegerField()
    Email=models.EmailField(primary_key=True)
    Password=models.CharField(max_length=16)
    Door_No=models.CharField(max_length=10)
    Street=models.CharField(max_length=30)
    Area_Or_Village=models.CharField(max_length=30)
    City=models.CharField(max_length=30)

    def __str__(self):
        return  self.Name


class CheckoutModel(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zipcode= models.CharField(max_length=50)
    Country = models.CharField(max_length=50)


class Commentmodel(models.Model):
    user = models.ForeignKey(UserProfileSessionModel, on_delete=models.CASCADE)
    comment = models.TextField(max_length=350)
    image = models.ImageField(upload_to='comment_images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Replymodel(models.Model):
    user = models.ForeignKey(UserProfileSessionModel, on_delete=models.CASCADE)
    comment_by_user=models.ForeignKey(Commentmodel,on_delete=models.CASCADE ,default=None,null=False)
    admin=models.ForeignKey(Adminmodel,on_delete=models.CASCADE)
    reply=models.TextField(max_length=350)
    image=models.ImageField(upload_to='reply_images/')
    timestamp = models.DateTimeField(auto_now_add=True)
