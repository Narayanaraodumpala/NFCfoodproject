"""Swiggyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import  TemplateView

from Swiggyproject import settings
from s_adminapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
    path('register/',views.register,name='register'),
    path('admin_regiater_check/',views.admin_regiater_check,name='admin_regiater_check'),
    path('logout/',views.logout,name='logout'),


     path('state/',views.state,name='state'),
     path('save_state/',views.save_state,name='save_state'),
     path('update_sate/',views.update_sate,name='update_sate'),
     path('update_save_state/',views.update_save_state,name='update_save_state'),
     path('delate_save_state/', views.delate_save_state, name='delate_sate'),
     path('city/',views.city,name='city'),
     path('city_save/',views.city_save,name='city_save'),
     path('Area/',views.area,name='Area'),
     path('area_save/',views.area_save,name='area_save'),
     path('Type_of_Place/',views.type_of_Place,name='Type_of_Place'),
     path('save_rest_type/', views.save_rest_type, name='save_rest_type'),
     path('add_food/', views.Add_food.as_view(), name='add_food'),
     path('view_food/',views.View_food.as_view(),name='view_food'),
     path('veg_food/',views.veg_food,name='veg_food'),
    path('non_veg/',views.non_veg,name='non_veg'),
    path('sea_food/',views.sea_food,name='sea_food'),
    path('desserts/',views.desserts,name='desserts'),
    path('drinks/',views.drinks,name='drimks'),
    path('all_types/',views.All_types.as_view(),name='all_foods'),
    path('about/',views.about,name='about'),
    path('careers/',views.careesr,name='careers'),
    path('contact/',views.contact,name='contact'),
    path('code_of_conduct/',views.code_of_conduct,name='code_of_conduct'),
    path('community/',views.community,name='community'),
    path('developers/',views.developers,name='developers'),
    path('privacy/',views.privacy,name='privacy'),
    path('terms/',views.terms,name='terms'),
    path('security/',views.security,name='security'),

    path('order_dish/',views.order_dish,name='order_dish'),
    path('user_login/', views.user_login, name='user_login'),
    path('validate_otp/', views.validate_otp, name='validate_otp'),
    path('save_user/', views.Save_user, name='save_user'),
    path('email/', views.email, name='email'),
    path('order_place/', views.order_place, name='order_place'),
    path('confirm_Order/', views.confirm_Order, name='confirm_Order'),
    path('get_Order/',views.get_Order,name='get_Order')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)