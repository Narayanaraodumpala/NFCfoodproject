from  django import forms
from  restarent.models import *

class restaurentform(forms.ModelForm):
    Restaurant_Password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model=RestarentModel
        fields="__all__"
        exclude=('Restaurant_Id','Restaurant_Otp','Restaurant_Status')
class rest_login_form(forms.Form):
     Restaurent_Email=forms.EmailField()
     Restaurent_password=forms.CharField(widget=forms.PasswordInput)
class Type_of_foodform(forms.ModelForm):
    class Meta:
        model=Type_of_foodmodel
        fields="__all__"

class Food_form(forms.ModelForm):
    class Meta:
        model=Food_model
        fields="__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields="__all__"
class SessionForm(forms.ModelForm):
    class Meta:
        model=UserProfileSessionModel
        fields="__all__"
class CommentForm(forms.ModelForm):
    class Meta:
        model=Commentmodel
        fields="__all__"

class ReplyForm(forms.ModelForm):
    class Meta:
        model=Replymodel
        fields="__all__"