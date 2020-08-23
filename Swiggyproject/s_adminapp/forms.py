from django import forms


from s_adminapp.models import *

class Admin_LoginForm(forms.ModelForm):
    class Meta:
        model=Adminmodel
        fields="__all__"

class StateForm(forms.ModelForm):
    class Meta:
        model=StateModel
        fields = ('State_Name',)

class CityForm(forms.ModelForm):
    class Meta:
        model=CityModel
        fields="__all__"
        exclude=('City_No',)
class AreaForm(forms.ModelForm):
    class Meta:
        model=AreaModel
        fields="__all__"
        exclude=('Area_No',)

class Type_of_plce(forms.ModelForm):
    class Meta:
        model=Type_of_resModel
        fields=('Type_Of_Place',)
class UserregisterForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields='__all__'
