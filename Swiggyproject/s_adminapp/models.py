from django.db import models

# Create your models here.
class Adminmodel(models.Model):
    User_Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=8)

    def __str__(self):
        return self.User_Name

class StateModel(models.Model):
    State_no=models.AutoField(primary_key=True)
    State_Name=models.CharField(max_length=30,unique=True)
    def __str__(self):
      return self.State_Name

class CityModel(models.Model):
    City_No=models.AutoField(primary_key=True)
    City_Name=models.CharField(max_length=40,unique=True)
    State_Name=models.ForeignKey(StateModel,on_delete=models.CASCADE)

    def __str__(self):
       return self.City_Name

class AreaModel(models.Model):
    Area_No=models.AutoField(primary_key=True)
    Area_Name=models.CharField(max_length=30,unique=True)
    City_Name=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Area_Name
class Type_of_resModel(models.Model):
     Type_No=models.AutoField(primary_key=True)
     Type_Of_Place=models.CharField(max_length=40)

     def __str__(self):
         return  self.Type_Of_Place
class UserModel(models.Model):
      Email=models.CharField(primary_key=True,max_length=30)
      Password=models.IntegerField()
      Name=models.CharField(max_length=30,default=None)
      Age=models.IntegerField(default=None)
      Phone=models.IntegerField(default=None)
      Gender=models.CharField(max_length=7,default=None)
      Door_No=models.CharField(max_length=7,default=None)
      Street=models.CharField(max_length=30,default=None)
      Area_Or_Village=models.CharField(max_length=30,default=None)
      City=models.CharField(max_length=30,default=None)
class orderFoodModel(models.Model):
    F_id=models.AutoField(primary_key=True)
    F_name=models.CharField(max_length=30)
    F_price=models.FloatField()
    F_image=models.ImageField(upload_to='orders/')
    F_type=models.CharField(max_length=30)